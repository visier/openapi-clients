import argparse
import copy
import logging
import os

import yaml

special_operations = {
    'Authentication_ASIDTokenAuthentication': 'asid_token_authentication',
    'OAuth2_OAuth2Authorize': 'oauth2_authorize'
}

# Constants for YAML keys
PATHS = 'paths'
OPERATION_ID = 'operationId'
TAGS = 'tags'
METHODS = ['get', 'post', 'put', 'delete', 'patch']

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCHEMA_COMPONENT_MAP = {
    # Top-level namespaces
    "google": "Goo_",
    "protobuf": "Proto_",
    "admin": "Adm_",
    "data": "Dat_",
    "jobs": "Job_",
    "analysis": "Anls_",
    "common": "Cmn_",
    "authentication": "Auth_",
    "data_in": "DIn_",
    "data_out": "DOut_",
    "dataservices": "DSvc_",
    "datamodel": "DMod_",
    "query": "Qry_",
    "designer": "Design_",
    "api": "Api_",
    "crypto": "Crypt_",
    "webhook": "WHook_",
    "dp": "Dp_",
    "dp_automation": "DpAuto_",
    "planning": "Plan_",
    "servicing": "Svc_",
    "objectconfiguration": "ObjCfg_",
    "v2": "V2_",
    "systemstatus": "SysSt_",
}


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False)


def find_null_schemas(spec):
    null_schemas = []
    for path, methods in spec.get('paths', {}).items():
        for method, details in methods.items():
            if 'requestBody' in details:
                content = details['requestBody'].get('content', {})
                if 'application/json' in content:
                    schema = content['application/json'].get('schema')
                    if schema is None:
                        null_schemas.append(f"Null schema found in endpoint: {method.upper()} {path}")
    return null_schemas


def update_operation_ids(spec):
    updated_spec = copy.deepcopy(spec)
    for path, methods in spec.get(PATHS, {}).items():
        for method in methods:
            if method in METHODS:
                operation = methods[method]
                if OPERATION_ID in operation and TAGS in operation and operation[TAGS]:
                    # Tag(ServiceName) is used as a prefix for all operationIds. (ServiceName_OperationName)
                    # It should be removed to make method names more readable.
                    first_tag = operation[TAGS][0]

                    operation_id = operation[OPERATION_ID]
                    new_operation_id = None
                    if operation_id in special_operations:
                        new_operation_id = special_operations[operation_id]
                    elif operation_id.startswith(first_tag):
                        new_operation_id = operation_id[len(first_tag) + 1:]
                    if new_operation_id:
                        updated_spec[PATHS][path][method][OPERATION_ID] = new_operation_id
    return updated_spec


def get_updated_schema_name(qualified_name, schema_map):
    parts = qualified_name.split('.')
    for i, part in enumerate(parts):
        if part in schema_map:
            parts[i] = schema_map[part]
    return ''.join(parts)


def get_schema_update_map(spec: dict):
    schemas = spec['components']['schemas']
    schema_name_mapping = {}
    for schema_name in schemas:
        # Get the updated schema name
        updated_schema_name = get_updated_schema_name(schema_name, SCHEMA_COMPONENT_MAP)
        schema_name_mapping[schema_name] = updated_schema_name
    return schema_name_mapping


def update_refs_recursively(spec, schema_name_mapping):
    if isinstance(spec, dict):
        # Check if this is a $ref object
        if '$ref' in spec and spec['$ref'].startswith('#/components/schemas/'):
            # Extract the schema name from the reference
            ref_parts = spec['$ref'].split('/')
            schema_name = ref_parts[-1]

            # If this schema name is in our mapping, update the reference
            if schema_name in schema_name_mapping:
                new_schema_name = schema_name_mapping[schema_name]
                spec['$ref'] = f'#/components/schemas/{new_schema_name}'

        # Recursively process all dictionary values
        for key, value in spec.items():
            spec[key] = update_refs_recursively(value, schema_name_mapping)

    elif isinstance(spec, list):
        # Recursively process all list items
        for i, item in enumerate(spec):
            spec[i] = update_refs_recursively(item, schema_name_mapping)

    return spec


def update_schema_names(orig_spec):
    spec = copy.deepcopy(orig_spec)
    update_schema_map = get_schema_update_map(spec)        
    update_refs_recursively(spec, update_schema_map)
    for schema_name in update_schema_map:
        # Update the schema name in the components section
        spec['components']['schemas'][update_schema_map[schema_name]] = spec['components']['schemas'][schema_name]
        del spec['components']['schemas'][schema_name]
        logging.info(f"Updated schema name from {schema_name} to {update_schema_map[schema_name]}")
        
    return spec


def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    error_code = 0
    for filename in os.listdir(input_dir):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)

            spec = load_yaml(input_file_path)
            errors = find_null_schemas(spec)
            if len(errors) > 0:
                logging.error(f"File: {filename}")
                for log in errors:
                    logging.error(log)
                error_code = 1

            updated_spec = update_operation_ids(spec)
            updated_spec = update_schema_names(updated_spec)
            save_yaml(updated_spec, output_file_path)
            logging.info(f"Processed {filename} and saved updated specification to {output_file_path}")

    return error_code


def main():
    parser = argparse.ArgumentParser(
        description="Update OpenAPI specifications by removing the first tag from operationId.")
    parser.add_argument("input_dir", help="Directory containing the YAML files to process.")
    parser.add_argument("output_dir", help="Directory to save the updated YAML files.")

    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()

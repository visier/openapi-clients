import argparse
import copy
import enum
import logging
import os
import sys
from typing import Dict, List, Tuple, Union, Any, Optional

import yaml
from yaml.representer import SafeRepresenter

# This is to ensure that multi-line strings are represented correctly in YAML
# "|" will be used for multi-line strings as it is in original YAML file
def represent_multiline_str(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
yaml.SafeDumper.add_representer(str, represent_multiline_str)

# Special operations mapping
special_operations = {
    'Authentication_ASIDTokenAuthentication': 'asid_token_authentication',
    'OAuth2_OAuth2Authorize': 'oauth2_authorize'
}

# Constants for YAML keys
PATHS = 'paths'
OPERATION_ID = 'operationId'
TAGS = 'tags'
METHODS = ['get', 'post', 'put', 'delete', 'patch']
COMPONENTS = 'components'
SCHEMAS = 'schemas'
REF = '$ref'
COMPONENTS_SCHEMAS_REF = '#/components/schemas/'
REQUEST_BODY = 'requestBody'
CONTENT = 'content'
APPLICATION_JSON = 'application/json'
SCHEMA = 'schema'

# File extensions
YAML_EXT = '.yaml'
YML_EXT = '.yml'

# Error codes
class ErrorCode(enum.Enum):
    SUCCESS_CODE = 0
    NULL_SCHEMA_ERROR = 10
    SCHEMA_QUALIFIED_NAME_ERROR = 20

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
    "designer": "Dsgn_",
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


def load_yaml(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w') as file:
        yaml.dump(data, file, Dumper=yaml.SafeDumper, sort_keys=False, default_flow_style=False)



def find_null_schemas(spec: Dict[str, Any]) -> List[str]:
    null_schemas = []
    for path, methods in spec.get(PATHS, {}).items():
        for method, details in methods.items():
            if REQUEST_BODY in details:
                content = details[REQUEST_BODY].get(CONTENT, {})
                if APPLICATION_JSON in content:
                    schema = content[APPLICATION_JSON].get(SCHEMA)
                    if schema is None:
                        null_schemas.append(f"Null schema found in endpoint: {method.upper()} {path}")
    return null_schemas


def update_operation_ids(spec: Dict[str, Any]) -> Dict[str, Any]:
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


def get_updated_schema_name(qualified_name: str, schema_map: Dict[str, str]) -> str:
    parts = qualified_name.split('.')
    for i, part in enumerate(parts):
        if part in schema_map:
            parts[i] = schema_map[part]
    return ''.join(parts)


def get_schema_update_map(spec: dict):
    schemas = spec[COMPONENTS][SCHEMAS]
    schema_name_mapping = {}
    for schema_name in schemas:
        # Check if the schema name contains multiple components
        if '.' in schema_name:
            updated_schema_name = get_updated_schema_name(schema_name, SCHEMA_COMPONENT_MAP)
            schema_name_mapping[schema_name] = updated_schema_name
    return schema_name_mapping


def update_refs_recursively(spec: Union[Dict[str, Any], List[Any]], schema_name_mapping: Dict[str, str]) -> Union[Dict[str, Any], List[Any]]:
    if isinstance(spec, dict):
        if REF in spec and spec[REF].startswith(COMPONENTS_SCHEMAS_REF):
            # Extract the schema name from the $ref
            ref_parts = spec[REF].split('/')
            schema_name = ref_parts[-1]
            if schema_name in schema_name_mapping:
                new_schema_name = schema_name_mapping[schema_name]
                spec[REF] = f'{COMPONENTS_SCHEMAS_REF}{new_schema_name}'

        for key, value in spec.items():
            # Recursively process all dictionary values
            spec[key] = update_refs_recursively(value, schema_name_mapping)

    elif isinstance(spec, list):
        # Recursively process all list items
        for i, item in enumerate(spec):
            spec[i] = update_refs_recursively(item, schema_name_mapping)

    return spec


def update_schema_names(orig_spec: Dict[str, Any]) -> Tuple[Dict[str, Any], ErrorCode]:
    spec = copy.deepcopy(orig_spec)
    update_schema_map = get_schema_update_map(spec)
    schema_errors = []
    for schema_name in list(spec[COMPONENTS][SCHEMAS].keys()):
        if '.' in schema_name:
            parts = schema_name.split('.')
            # Check that all parts except the last one are in SCHEMA_COMPONENT_MAP
            namespace_parts = parts[:-1]
            for part in namespace_parts:
                if part not in SCHEMA_COMPONENT_MAP:
                    schema_errors.append(f"Schema part '{part}' in '{schema_name}' not found in SCHEMA_COMPONENT_MAP")
                    
    if schema_errors:
        for error in schema_errors:
            logging.error(error)
        return spec, ErrorCode.SCHEMA_QUALIFIED_NAME_ERROR
    
    update_refs_recursively(spec, update_schema_map)
    for schema_name in update_schema_map:
        # Update the schema name in the components section
        spec[COMPONENTS][SCHEMAS][update_schema_map[schema_name]] = spec[COMPONENTS][SCHEMAS][schema_name]
        del spec[COMPONENTS][SCHEMAS][schema_name]
        logging.info(f"Updated schema name from {schema_name} to {update_schema_map[schema_name]}")
    
    return spec, ErrorCode.SUCCESS_CODE


def process_file(input_file_path: str, output_file_path: str) -> ErrorCode:
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    spec = load_yaml(input_file_path)
    errors = find_null_schemas(spec)
    
    if len(errors) > 0:
        logging.error(f"File: {os.path.basename(input_file_path)}")
        for log in errors:
            logging.error(log)
        return ErrorCode.NULL_SCHEMA_ERROR

    updated_spec = update_operation_ids(spec)
    updated_spec, schema_error_code = update_schema_names(updated_spec)
    
    # Update error code if schema errors were found
    if schema_error_code != ErrorCode.SUCCESS_CODE:
        logging.error(f"Schema validation errors found in {os.path.basename(input_file_path)}")
        return schema_error_code

    save_yaml(updated_spec, output_file_path)
    logging.info(f"Processed {os.path.basename(input_file_path)} and saved updated specification to {output_file_path}")
    return ErrorCode.SUCCESS_CODE


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update OpenAPI specifications by removing the first tag from operationId.")
    parser.add_argument("input_file", help="Path to the YAML file to process.")
    parser.add_argument("output_file", help="Path where the updated YAML file will be saved.")

    args = parser.parse_args()

    error_code = process_file(args.input_file, args.output_file)
    sys.exit(error_code.value)


if __name__ == "__main__":
    main()

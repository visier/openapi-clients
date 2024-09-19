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

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)


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
            save_yaml(updated_spec, output_file_path)
            logging.info(f"Processed {filename} and saved updated specification to {output_file_path}")

    return error_code


def main():
    parser = argparse.ArgumentParser(
        description="Update OpenAPI specifications by removing the first tag from operationId.")
    parser.add_argument("input_dir", help="Directory containing the YAML files to process.")
    parser.add_argument("output_dir", help="Directory to save the updated YAML files.")

    args = parser.parse_args()

    error_code = process_directory(args.input_dir, args.output_dir)
    # TODO uncomment sys.exit(error_code)


if __name__ == "__main__":
    main()

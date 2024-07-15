import argparse
import copy
import os

import yaml

prefix_to_postfix = ['V1', 'V1Alpha', 'V2', 'V2Alpha', 'V3', 'V3Alpha', 'V4', 'V4Alpha', 'V5', 'V5Alpha']
special_operations = {
    'Authentication_ASIDTokenAuthentication': 'asid_token_authentication',
    'OAuth2_OAuth2Authorize': 'oauth2_authorize'
}

# Constants for YAML keys
PATHS = 'paths'
OPERATION_ID = 'operationId'
TAGS = 'tags'
METHODS = ['get', 'post', 'put', 'delete', 'patch']


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def save_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.safe_dump(data, file)


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
                        # To avoid operationIds collisions there will be added versions of the methods
                        for postfix in prefix_to_postfix:
                            if first_tag.endswith(postfix):
                                new_operation_id = f"{new_operation_id}_{postfix}"
                                break
                    if new_operation_id:
                        updated_spec[PATHS][path][method][OPERATION_ID] = new_operation_id
    return updated_spec


def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)

            spec = load_yaml(input_file_path)
            updated_spec = update_operation_ids(spec)
            save_yaml(updated_spec, output_file_path)

            print(f"Processed {filename} and saved updated specification to {output_file_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Update OpenAPI specifications by removing the first tag from operationId.")
    parser.add_argument("input_dir", help="Directory containing the YAML files to process.")
    parser.add_argument("output_dir", help="Directory to save the updated YAML files.")

    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()

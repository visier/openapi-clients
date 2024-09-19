import os
import sys

import yaml


def find_null_schemas(file_path):
    with open(file_path, 'r') as file:
        spec = yaml.safe_load(file)

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


def main():
    if len(sys.argv) != 2:
        print("Usage: python schema_validator.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    problem_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                null_schemas = find_null_schemas(file_path)
                if null_schemas:
                    print(f"File: {file_path}")
                    for log in null_schemas:
                        print(log)
                    print("\n")
                    problem_count += len(null_schemas)
    sys.exit(problem_count)


if __name__ == "__main__":
    main()

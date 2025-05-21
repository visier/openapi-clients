#!/usr/bin/env python3

import yaml
import argparse
import sys

def extract_schemas(input_file: str, output_file: str) -> None:
    """
    Extract all schemas from an OpenAPI YAML file and write them to the output file.
    
    Args:
        input_file (str): Path to the input OpenAPI YAML file
        output_file (str): Path to the output file where schemas will be stored
    """
    try:
        # Load the YAML file
        with open(input_file, 'r') as f:
            openapi_spec = yaml.safe_load(f)
        
        # Check if components and schemas exist in the OpenAPI spec
        if 'components' not in openapi_spec or 'schemas' not in openapi_spec['components']:
            print(f"Error: No schemas found in {input_file}")
            sys.exit(1)
        
        # Extract all schema names
        schemas = openapi_spec['components']['schemas']
        schema_names = list(schemas.keys())
        
        # Write schema names to the output file
        with open(output_file, 'w') as f:
            for name in schema_names:
                f.write(f"{name}\n")
        
        print(f"Successfully extracted {len(schema_names)} schema names to {output_file}")
    
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract schemas from OpenAPI YAML file')
    parser.add_argument('-i', '--input', required=True, help='Input OpenAPI YAML file')
    parser.add_argument('-o', '--output', required=True, help='Output file to store schemas')
    
    args = parser.parse_args()
    
    # Extract schemas
    extract_schemas(args.input, args.output)

if __name__ == '__main__':
    main()
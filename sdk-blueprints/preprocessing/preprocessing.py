import argparse
import copy
import enum
import logging
import os
import sys
from typing import Dict, List, Tuple, Union, Any, cast

import yaml

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


# Error codes
class ErrorCode(enum.IntEnum):
    SUCCESS_CODE = 0
    NULL_SCHEMA_ERROR = 10
    SCHEMA_DTO_DUPLICATION = 20


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SCHEMA_COMPONENT_MAP = {
    "dataservices.datamodel.AnalyticObjectDTO": "DataModelAnalyticObjectDTO",
    "dataservices.datamodel.AnalyticObjectDTOs": "DataModelAnalyticObjectDTOs",
    "designer.api.DimensionFilterDTO": "DesignerDimensionFilterDTO",
    "designer.api.SelectionConceptDTO": "DesignerSelectionConceptDTO",
    "servicing.DirectDataUploadFileResponseDTO": "ServicingDirectDataUploadFileResponseDTO",
    "servicing.v2.objectconfiguration.CalculatedPropertyTypeDTO": "V2CalculatedPropertyTypeDTO",
    "servicing.v2.objectconfiguration.DimensionDTO": "V2DimensionDTO",
    "servicing.v2.objectconfiguration.LevelDTO": "V2LevelDTO",
    "servicing.v2.objectconfiguration.SimplePropertyTypeDTO": "V2SimplePropertyTypeDTO",
}


def represent_multiline_str(dumper, data):
    """
    Preserves multi-line string formatting in YAML output.
    
    Args:
        dumper: YAML dumper instance
        data: String data to be represented
        
    Returns:
        YAML scalar with '|' style for multi-line strings
    """
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.SafeDumper.add_representer(str, represent_multiline_str)


def load_yaml(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def save_yaml(data: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w') as file:
        yaml.dump(data, file, Dumper=yaml.SafeDumper, sort_keys=False, default_flow_style=False)


def find_null_schemas(spec: Dict[str, Any]) -> List[str]:
    """
    Identifies endpoints with missing schema definitions in request bodies.
    
    Args:
        spec: OpenAPI specification dictionary
        
    Returns:
        List of error messages for endpoints with null schemas
    """
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
    """
    Removes service name prefixes from operation IDs for improved readability.
    
    Args:
        spec: OpenAPI specification dictionary
        
    Returns:
        Updated specification with cleaner operation IDs
    """
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


def get_all_schema_mappings(spec: Dict[str, Any], schema_component_map: Dict[str, str]) -> Dict[str, str]:
    """
    Creates mappings for schema names to make them more concise.
    
    Args:
        spec: OpenAPI specification dictionary
        schema_component_map: Predefined mappings for specific schema names
        
    Returns:
        Dictionary mapping original schema names to simplified names
    """
    schema_mappings = {}
    for schema_name in spec[COMPONENTS][SCHEMAS]:
        # If the schema name is in our mapping, add it to the result
        if schema_name in schema_component_map:
            schema_mappings[schema_name] = schema_component_map[schema_name]
        else:
            # Otherwise, just use the last part of the schema name
            schema_mappings[schema_name] = schema_name.split('.')[-1]

    return schema_mappings


def update_schema_refs_recursively(
        update_spec: Union[Dict[str, Any], List[Any], Any],
        schema_name_mapping: Dict[str, str]
) -> Union[Dict[str, Any], List[Any], Any]:
    """
    Recursively updates schema references throughout the specification.
    
    Args:
        update_spec: Part of OpenAPI spec being processed (dict, list or primitive)
        schema_name_mapping: Mapping of original schema names to new names
        
    Returns:
        Updated specification part with replaced references
    """
    if isinstance(update_spec, dict):
        result = {}
        for key, value in update_spec.items():
            if key == REF and isinstance(value, str) and value.startswith(COMPONENTS_SCHEMAS_REF):
                # Extract the schema name from the reference
                ref_parts = value.split('/')
                schema_name = ref_parts[-1]
                if schema_name in schema_name_mapping:
                    new_schema_name = schema_name_mapping[schema_name]
                    result[key] = f'{COMPONENTS_SCHEMAS_REF}{new_schema_name}'
                else:
                    # Keep the original reference if no mapping exists
                    result[key] = value
            else:
                # Recursively process nested structures
                result[key] = update_schema_refs_recursively(value, schema_name_mapping)
        return result
    elif isinstance(update_spec, list):
        return [update_schema_refs_recursively(item, schema_name_mapping) for item in update_spec]
    else:
        # Return primitive values as is
        return update_spec


def update_schema_names(orig_spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Updates schema names and references throughout the specification.
    
    Args:
        orig_spec: Original OpenAPI specification dictionary
        
    Returns:
        Updated specification with renamed schemas and updated references
    """
    schema_mappings = get_all_schema_mappings(orig_spec, SCHEMA_COMPONENT_MAP)
    update_spec_result = update_schema_refs_recursively(copy.deepcopy(orig_spec), schema_mappings)
    # Casting to Dict[str, Any] to avoid linter errors
    update_spec = cast(Dict[str, Any], update_spec_result)
    update_schemas = update_spec[COMPONENTS][SCHEMAS]

    for orig_schema_name in list(update_schemas.keys()):
        if orig_schema_name in schema_mappings:
            new_schema_name = schema_mappings[orig_schema_name]
            if new_schema_name != orig_schema_name:
                # Update the schema name in the components section
                schema_content = update_schemas[orig_schema_name]
                del update_schemas[orig_schema_name]
                update_schemas[new_schema_name] = schema_content
                logging.info(f"Replaced schema `{orig_schema_name}` with `{new_schema_name}`")
    return update_spec


def has_duplicated_dto_names(spec: Dict[str, Any]) -> bool:
    """
    Checks for duplicate DTO names in the specification.
    
    Args:
        spec: OpenAPI specification dictionary
        
    Returns:
        True if duplicates exist, False otherwise
    """
    dto_names: Dict[str, List[str]] = {}
    for schema_name in spec.get(COMPONENTS, {}).get(SCHEMAS, {}):
        # Extract the DTO name from the qualified schema name
        dto_name = schema_name.split('.')[-1]
        dto_names.setdefault(dto_name, []).append(schema_name)

    has_duplicates = False
    for dto_name, schemas in dto_names.items():
        if len(schemas) > 1:
            for schema in schemas:
                logging.error(f"Duplicate schema name '{dto_name}' found: {schema}")
            has_duplicates = True
    if not has_duplicates:
        logging.info("No duplicate DTO names were found.")
    return has_duplicates


def update_specification(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], ErrorCode]:
    """
    Validates and transforms the OpenAPI specification.
    
    Args:
        spec: Original OpenAPI specification dictionary
        
    Returns:
        Tuple containing:
        - Updated specification (or empty dict if validation fails)
        - Error code indicating success or specific failure reason
    """
    errors = find_null_schemas(spec)
    if len(errors) > 0:
        for log in errors:
            logging.error(log)
        return {}, ErrorCode.NULL_SCHEMA_ERROR

    updated_spec = update_operation_ids(spec)
    updated_spec = update_schema_names(updated_spec)

    if has_duplicated_dto_names(updated_spec):
        return {}, ErrorCode.SCHEMA_DTO_DUPLICATION

    return updated_spec, ErrorCode.SUCCESS_CODE


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Processes OpenAPI specifications by: 1) removing service name prefixes from operation IDs, 2) replacing schema names with more readable values, 3) validating specifications for null schemas and duplicate DTO names. Can either validate specifications without modification or save the updated version."

    )
    parser.add_argument("-i", "--input", dest="input_file", required=True,
                        help="Path to the YAML file to process.")
    output_group = parser.add_mutually_exclusive_group(required=True)
    output_group.add_argument("-o", "--output", dest="output_file",
                              help="Path where the updated YAML file will be saved.")
    output_group.add_argument("-v", "--validate", action="store_true",
                              help="Only validate the schema without saving it.")

    args = parser.parse_args()

    spec = load_yaml(args.input_file)
    updated_spec, error_code = update_specification(spec)

    if error_code != ErrorCode.SUCCESS_CODE:
        logging.error(f"Validation failed with error code: {error_code}")
        sys.exit(error_code.value)

    if args.validate:
        logging.info(f"Validation successful for {args.input_file}")
    else:
        output_dir = os.path.dirname(args.output_file)
        # Create output directory if it doesn't exist
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        save_yaml(updated_spec, args.output_file)
        logging.info(
            f"Processed {os.path.basename(args.input_file)} and saved updated specification to {args.output_file}")

    sys.exit(error_code.value)


if __name__ == "__main__":
    main()

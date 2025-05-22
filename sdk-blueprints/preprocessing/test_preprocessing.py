import os
import tempfile
import unittest
import copy
from unittest import mock

import preprocessing

# Get the directory of the current script for relative paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Test file paths
TEST_SPECS_DIR = 'test_specs'
BASIC_SPEC_FILE = 'basic_spec.yaml'
NULL_SCHEMA_SPEC_FILE = 'null_schema_spec.yaml'
DUPLICATE_DTO_SPEC_FILE = 'duplicate_dto_spec.yaml'
SPECIAL_OPS_SPEC_FILE = 'special_operations_spec.yaml'
SCHEMA_MAPPING_SPEC_FILE = 'schema_mapping_spec.yaml'

# Common test data
API_TITLE = 'Basic Test API'
API_VERSION = '1.0.0'
VALID_ENDPOINT_PATH = '/valid-endpoint'
VALID_OPERATION_ID = 'ValidOperation'

# Schema constants
COMPONENTS_SCHEMAS_REF_PREFIX = '#/components/schemas/'
COMPONENTS_KEY = 'components'
SCHEMAS_KEY = 'schemas'
REF_KEY = '$ref'
PATHS_KEY = 'paths'
INFO_KEY = 'info'
TITLE_KEY = 'title'
VERSION_KEY = 'version'
POST_METHOD = 'post'
OPERATION_ID_KEY = 'operationId'
REQUEST_BODY_KEY = 'requestBody'
CONTENT_KEY = 'content'
APPLICATION_JSON = 'application/json'
SCHEMA_KEY = 'schema'

# CLI arguments
CLI_SCRIPT_NAME = 'preprocessing.py'
CLI_INPUT_ARG = '-i'
CLI_OUTPUT_ARG = '-o'
CLI_VALIDATE_ARG = '-v'
TEST_INPUT_FILE = 'input.yaml'
TEST_OUTPUT_FILE = 'output.yaml'


class TestProcessing(unittest.TestCase):
    def setUp(self):
        # Load common test specs
        self.basic_spec_path = os.path.join(SCRIPT_DIR, TEST_SPECS_DIR, BASIC_SPEC_FILE)
        self.null_schema_spec_path = os.path.join(SCRIPT_DIR, TEST_SPECS_DIR, NULL_SCHEMA_SPEC_FILE)
        self.duplicate_dto_spec_path = os.path.join(SCRIPT_DIR, TEST_SPECS_DIR, DUPLICATE_DTO_SPEC_FILE)

        self.basic_spec = preprocessing.load_yaml(self.basic_spec_path)
        self.special_ops_spec = preprocessing.load_yaml(os.path.join(SCRIPT_DIR, TEST_SPECS_DIR, SPECIAL_OPS_SPEC_FILE))
        self.schema_mapping_spec = preprocessing.load_yaml(
            os.path.join(SCRIPT_DIR, TEST_SPECS_DIR, SCHEMA_MAPPING_SPEC_FILE))
            
    def compare_dicts(self, dict1, dict2, ignore_order=True):
        """
        Compare two dictionaries recursively and return differences.
        
        Args:
            dict1: First dictionary to compare
            dict2: Second dictionary to compare
            ignore_order: Whether to ignore order in lists
            
        Returns:
            Empty dictionary if no differences, otherwise a dictionary of differences
        """
        if type(dict1) != type(dict2):
            return {f"type_mismatch": f"{type(dict1)} != {type(dict2)}"}
            
        if isinstance(dict1, dict):
            differences = {}
            
            # Check for keys in dict1 that are not in dict2
            for key in dict1:
                if key not in dict2:
                    differences[f"missing_key_in_second"] = key
                    continue
                    
                # Recursively compare values
                value_diff = self.compare_dicts(dict1[key], dict2[key], ignore_order)
                if value_diff:
                    differences[f"value_diff_at_{key}"] = value_diff
                    
            # Check for keys in dict2 that are not in dict1
            for key in dict2:
                if key not in dict1:
                    differences[f"missing_key_in_first"] = key
                    
            return differences
            
        elif isinstance(dict1, list) and ignore_order:
            if len(dict1) != len(dict2):
                return {f"length_mismatch": f"{len(dict1)} != {len(dict2)}"}
                
            # For simplicity, we'll just check if all items in dict1 are in dict2
            # This is not a perfect comparison for lists of complex objects
            for item1 in dict1:
                found = False
                for item2 in dict2:
                    if not self.compare_dicts(item1, item2, ignore_order):
                        found = True
                        break
                if not found:
                    return {f"item_not_found": f"{item1}"}
                    
            return {}
            
        elif isinstance(dict1, list):
            if len(dict1) != len(dict2):
                return {f"length_mismatch": f"{len(dict1)} != {len(dict2)}"}
                
            differences = {}
            for i, (item1, item2) in enumerate(zip(dict1, dict2)):
                item_diff = self.compare_dicts(item1, item2, ignore_order)
                if item_diff:
                    differences[f"item_diff_at_{i}"] = item_diff
                    
            return differences
            
        else:
            # Compare primitive values
            if dict1 != dict2:
                return {f"value_mismatch": f"{dict1} != {dict2}"}
                
            return {}

    def test_load_yaml(self):
        spec = preprocessing.load_yaml(self.basic_spec_path)
        self.assertEqual(spec[INFO_KEY][TITLE_KEY], API_TITLE)
        self.assertEqual(spec[INFO_KEY][VERSION_KEY], API_VERSION)

    def test_save_yaml(self):
        spec = preprocessing.load_yaml(self.basic_spec_path)

        with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as temp_file:
            temp_path = temp_file.name

        try:
            preprocessing.save_yaml(spec, temp_path)
            loaded_spec = preprocessing.load_yaml(temp_path)
            
            # Use our custom compare_dicts function to compare the entire dictionaries
            diff = self.compare_dicts(spec, loaded_spec, ignore_order=True)
            self.assertEqual(diff, {}, f"Differences found between original and loaded spec: {diff}")
            
            # Also keep the original specific checks for clarity
            self.assertEqual(loaded_spec[INFO_KEY][TITLE_KEY], spec[INFO_KEY][TITLE_KEY])
            self.assertEqual(loaded_spec[INFO_KEY][VERSION_KEY], spec[INFO_KEY][VERSION_KEY])
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_find_null_schemas(self):
        spec = preprocessing.load_yaml(self.null_schema_spec_path)
        null_schemas = preprocessing.find_null_schemas(spec)
        self.assertEqual(len(null_schemas), 1)
        self.assertIn("Null schema found in endpoint: POST /null-schema-endpoint", null_schemas)

        spec = preprocessing.load_yaml(self.basic_spec_path)
        null_schemas = preprocessing.find_null_schemas(spec)
        self.assertEqual(len(null_schemas), 0)

    def test_has_duplicated_dto_names(self):
        # Test with duplicate DTOs across different packages
        spec = preprocessing.load_yaml(self.duplicate_dto_spec_path)
        has_duplicates = preprocessing.has_duplicated_dto_names(spec)
        self.assertTrue(has_duplicates)

        # Test with duplicate DTOs in the same package
        spec_with_same_package_duplicates = {
            COMPONENTS_KEY: {
                SCHEMAS_KEY: {
                    'service1.dto.UserDTO': {},
                    'service1.api.UserDTO': {}
                }
            }
        }
        has_duplicates = preprocessing.has_duplicated_dto_names(spec_with_same_package_duplicates)
        self.assertTrue(has_duplicates)

        # Test with no duplicates
        no_dup_spec = {
            COMPONENTS_KEY: {
                SCHEMAS_KEY: {
                    'service1.api.ValidRequestDTO': {},
                    'service2.api.UniqueDTO': {}
                }
            }
        }
        has_duplicates = preprocessing.has_duplicated_dto_names(no_dup_spec)
        self.assertFalse(has_duplicates)

    def test_update_schema_refs_recursively(self):
        # Test simple reference update
        simple_ref = {REF_KEY: f'{COMPONENTS_SCHEMAS_REF_PREFIX}service1.api.ValidRequestDTO'}
        schema_mappings = {'service1.api.ValidRequestDTO': 'ValidRequestDTO'}
        updated_ref = preprocessing.update_schema_refs_recursively(simple_ref, schema_mappings)
        self.assertEqual(str(updated_ref), f"{{{REF_KEY!r}: '{COMPONENTS_SCHEMAS_REF_PREFIX}ValidRequestDTO'}}")

        # Test reference in a list
        list_with_ref = [
            {REF_KEY: f'{COMPONENTS_SCHEMAS_REF_PREFIX}dataservices.datamodel.AnalyticObjectDTO'},
            {'name': 'test'}
        ]
        schema_mappings = {'dataservices.datamodel.AnalyticObjectDTO': 'DataModelAnalyticObjectDTO'}
        updated_list = preprocessing.update_schema_refs_recursively(list_with_ref, schema_mappings)
        self.assertEqual(
            str(updated_list),
            f"[{{{REF_KEY!r}: '{COMPONENTS_SCHEMAS_REF_PREFIX}DataModelAnalyticObjectDTO'}}, {{'name': 'test'}}]"
        )

        # Test nested reference
        nested_ref = {'nested': {'deeper': {REF_KEY: f'{COMPONENTS_SCHEMAS_REF_PREFIX}custom.dto.TypeDTO'}}}
        schema_mappings = {'custom.dto.TypeDTO': 'TypeDTO'}
        updated_nested = preprocessing.update_schema_refs_recursively(nested_ref, schema_mappings)
        self.assertEqual(
            str(updated_nested),
            f"{{'nested': {{'deeper': {{{REF_KEY!r}: '{COMPONENTS_SCHEMAS_REF_PREFIX}TypeDTO'}}}}}}"
        )

    def test_update_schema_names(self):
        original_spec = copy.deepcopy(self.schema_mapping_spec)
        updated_spec = preprocessing.update_schema_names(self.schema_mapping_spec)

        schemas = updated_spec[COMPONENTS_KEY][SCHEMAS_KEY]
        
        # We need to account for the fact that schema references within schemas are also updated
        # So we can't directly compare the original and updated schemas
        # Instead, we'll check that the structure is preserved (types, properties, etc.)
        original_schemas = original_spec[COMPONENTS_KEY][SCHEMAS_KEY]
        
        # Create mappings to verify schema content was preserved
        schema_mappings = preprocessing.get_all_schema_mappings(original_spec, preprocessing.SCHEMA_COMPONENT_MAP)
        
        for orig_name, new_name in schema_mappings.items():
            if orig_name in original_schemas and new_name in schemas:
                # Get the original and updated schemas
                orig_schema = copy.deepcopy(original_schemas[orig_name])
                new_schema = schemas[new_name]
                
                # Check that the schema type is preserved
                if 'type' in orig_schema:
                    self.assertEqual(orig_schema['type'], new_schema['type'],
                                    f"Schema type changed for {orig_name} -> {new_name}")
                
                # Check that property names are preserved
                if 'properties' in orig_schema and 'properties' in new_schema:
                    orig_props = set(orig_schema['properties'].keys())
                    new_props = set(new_schema['properties'].keys())
                    self.assertEqual(orig_props, new_props,
                                    f"Property names changed for {orig_name} -> {new_name}")

        # Check that schema names were updated
        self.assertIn('DataModelAnalyticObjectDTO', schemas)
        self.assertIn('DataModelAnalyticObjectDTOs', schemas)
        self.assertIn('DesignerDimensionFilterDTO', schemas)
        self.assertIn('DesignerSelectionConceptDTO', schemas)
        self.assertIn('ServicingDirectDataUploadFileResponseDTO', schemas)

        # Check that old schema names were removed
        self.assertNotIn('dataservices.datamodel.AnalyticObjectDTO', schemas)
        self.assertNotIn('dataservices.datamodel.AnalyticObjectDTOs', schemas)
        self.assertNotIn('designer.api.DimensionFilterDTO', schemas)
        self.assertNotIn('designer.api.SelectionConceptDTO', schemas)
        self.assertNotIn('servicing.DirectDataUploadFileResponseDTO', schemas)

        # Check that references were updated
        endpoint_schema_ref = \
            updated_spec[PATHS_KEY]['/endpoint-with-mapped-schema'][POST_METHOD][REQUEST_BODY_KEY][CONTENT_KEY][
                APPLICATION_JSON][SCHEMA_KEY][REF_KEY]
        self.assertEqual(endpoint_schema_ref, f'{COMPONENTS_SCHEMAS_REF_PREFIX}DataModelAnalyticObjectDTO')

    def test_update_specification_success(self):
        spec = preprocessing.load_yaml(self.basic_spec_path)
        original_spec = copy.deepcopy(spec)
        updated_spec, error_code = preprocessing.update_specification(spec)

        self.assertEqual(error_code, preprocessing.ErrorCode.SUCCESS_CODE)
        
        # Check that operation IDs were updated correctly
        self.assertEqual(updated_spec[PATHS_KEY][VALID_ENDPOINT_PATH][POST_METHOD][OPERATION_ID_KEY],
                         VALID_OPERATION_ID)
        
        # Verify that the structure of the specification was preserved
        # We can't compare the entire dictionaries directly because we expect some changes
        # Instead, we'll check that the paths structure is preserved
        paths_diff = self.compare_dicts(
            list(original_spec[PATHS_KEY].keys()),
            list(updated_spec[PATHS_KEY].keys()),
            ignore_order=True
        )
        self.assertEqual(paths_diff, {}, f"Path structure changed: {paths_diff}")
        
        # Check that components structure is preserved (except for schema name changes)
        if COMPONENTS_KEY in original_spec and COMPONENTS_KEY in updated_spec:
            components_keys_diff = self.compare_dicts(
                {k: None for k in original_spec[COMPONENTS_KEY].keys()},
                {k: None for k in updated_spec[COMPONENTS_KEY].keys()},
                ignore_order=True
            )
            self.assertEqual(components_keys_diff, {}, f"Components structure changed: {components_keys_diff}")

    def test_update_specification_null_schema_error(self):
        spec = preprocessing.load_yaml(self.null_schema_spec_path)
        updated_spec, error_code = preprocessing.update_specification(spec)

        self.assertEqual(error_code, preprocessing.ErrorCode.NULL_SCHEMA_ERROR)
        self.assertEqual(updated_spec, {})

    def test_update_specification_duplicate_dto_error(self):
        # Create a spec with duplicate DTOs that will be detected after schema name transformation
        spec = {
            PATHS_KEY: {},
            COMPONENTS_KEY: {
                SCHEMAS_KEY: {
                    'service1.dto.UserDTO': {'type': 'object'},
                    'service2.dto.UserDTO': {'type': 'object'}
                }
            }
        }

        # Mock has_duplicated_dto_names to return True
        with mock.patch('preprocessing.has_duplicated_dto_names', return_value=True):
            updated_spec, error_code = preprocessing.update_specification(spec)
            self.assertEqual(error_code, preprocessing.ErrorCode.SCHEMA_DTO_DUPLICATION)
            self.assertEqual(updated_spec, {})

    @mock.patch('preprocessing.load_yaml')
    @mock.patch('preprocessing.save_yaml')
    @mock.patch('preprocessing.update_specification')
    def test_main(self, mock_update_spec, mock_save_yaml, mock_load_yaml):
        # Setup common mocks
        mock_load_yaml.return_value = {'test': 'spec'}

        # Test cases with different parameters and expected outcomes
        test_cases = [
            # (args, update_spec_return, expected_save_yaml_call, expected_exit_code)
            (
                [CLI_SCRIPT_NAME, CLI_INPUT_ARG, TEST_INPUT_FILE, CLI_OUTPUT_ARG, TEST_OUTPUT_FILE],  # Output mode
                ({'updated': 'spec'}, preprocessing.ErrorCode.SUCCESS_CODE),
                [mock.call({'updated': 'spec'}, TEST_OUTPUT_FILE)],
                0
            ),
            (
                [CLI_SCRIPT_NAME, CLI_INPUT_ARG, TEST_INPUT_FILE, CLI_VALIDATE_ARG],  # Validate mode
                ({'updated': 'spec'}, preprocessing.ErrorCode.SUCCESS_CODE),
                [],  # No save_yaml call expected
                0
            ),
            (
                [CLI_SCRIPT_NAME, CLI_INPUT_ARG, TEST_INPUT_FILE, CLI_VALIDATE_ARG],  # Error case
                ({}, preprocessing.ErrorCode.NULL_SCHEMA_ERROR),
                [],  # No save_yaml call expected
                preprocessing.ErrorCode.NULL_SCHEMA_ERROR.value
            )
        ]

        for args, update_spec_return, expected_save_yaml_calls, expected_exit_code in test_cases:
            # Reset mocks
            mock_update_spec.reset_mock()
            mock_save_yaml.reset_mock()
            mock_exit = mock.MagicMock()

            # Set return value for this test case
            mock_update_spec.return_value = update_spec_return

            # Run the test
            with mock.patch('sys.argv', args):
                with mock.patch('sys.exit', mock_exit):
                    preprocessing.main()

            # Verify expectations
            mock_load_yaml.assert_called_with(TEST_INPUT_FILE)
            mock_update_spec.assert_called_with({'test': 'spec'})

            if expected_save_yaml_calls:
                mock_save_yaml.assert_has_calls(expected_save_yaml_calls)
            else:
                mock_save_yaml.assert_not_called()

            mock_exit.assert_called_with(expected_exit_code)


if __name__ == '__main__':
    unittest.main()

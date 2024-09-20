import os
import sys


def update_unit_test_file(file_path):
    """Updates unit test file to fix generation issues."""

    file_name = os.path.basename(file_path)
    if not file_name.startswith('test_'):
        return

    with open(file_path, 'r') as file:
        orig_content = file.read()

    if "(unittest.TestCase)" not in orig_content or "class Test" not in orig_content:
        return

    # Replace 'null' with 'None' in the content, as OpenAPI generator uses 'null' instead of 'None' for Python code.
    content = orig_content.replace('= null', '= None')

    # Workaround for EmptyAuthParamsDTO in data-in, where properties are empty (properties: {}).
    # OpenAPI generator does not generate the model for it and replaces it with a dictionary.
    if (file_path.endswith('visier_api_data_in/test/test_data_provider_auth_information_dto.py')
            or file_path.endswith('visier_api_data_in/test/test_data_provider_auth_params_dto.py')):
        content = content.replace(
            'empty_auth_params = visier_api_data_in.models.empty_auth_params_dto.EmptyAuthParamsDTO()',
            'empty_auth_params = {}'
        )

    if content == orig_content:
        print(f"There is no need to update unit test {file_path}.")
    else:
        print(f"Updating file: {file_path}")
        with open(file_path, 'w') as file:
            file.write(content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        update_unit_test_file(sys.argv[1])
    else:
        print("Please provide the python file path as an argument.")

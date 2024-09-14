import os
import re
import sys


def process_file(file_path):
    file_name = os.path.basename(file_path)
    if not file_name.startswith('test_'):
        return

    with open(file_path, 'r') as file:
        orig_content = file.read()

    if "(unittest.TestCase)" not in orig_content or "class Test" not in orig_content:
        return

    # Replace 'null' with 'None'
    content = re.sub(r'\bnull\b', 'None', orig_content)

    if content == orig_content:
        print(f"There is no need to update unit test {file_path}.")
    else:
        print(f"Updating file: {file_path}")
        with open(file_path, 'w') as file:
            file.write(content)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_file(sys.argv[1])
    else:
        print("Please provide the python file path as an argument.")

import re

# Define the path to the input and output HTML files
input_file_path = './output/redoc-static.html'
output_file_path = './output/redoc-static.html'

# Read the HTML content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Define a regex pattern to remove the specific HTML comment
# This pattern looks for <!-- --> followed by optional whitespace
pattern = r"<!-- -->\s*"

# Substitute the pattern in the HTML content with an empty string
cleaned_html_content = re.sub(pattern, '', html_content)

# Write the cleaned HTML content to the output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_html_content)
import yaml
import re
import os

# Paths to the API spec files to combine
FILE_PATHS = {
    "authentication": "../res/authentication-apis.yaml",
    "data_in": "../res/data-in-apis.yaml",
    "data_out": "../res/data-out-apis.yaml",
    "administration": "../res/administration-apis.yaml",
    "analytic_model": "../res/analytic-model-apis.yaml",
    "skills_intelligence": "../res/skills-intelligence-engine.yaml",
    "compensation_benchmarks": "../res/compensation-benchmarks.yaml"
    }

EXCLUDED_TAGS = {}

def transform_tag_name(tag_name):
    spaced_tag_name = re.sub(r'([a-z])([A-Z])', r'\1 \2', tag_name)
    return spaced_tag_name

def transform_tag_group_name(group_name):
    return group_name.replace('_', ' ')

def replace_br_tags(description):
    return description.replace("<br>", "<br/>")

def escape_ampersands(description):
    return re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;)', '&amp;', description)

def process_descriptions(content):
    if isinstance(content, dict):
        for key, value in content.items():
            if key == "description" and isinstance(value, str):
                value = replace_br_tags(value)
                value = escape_ampersands(value)
                content[key] = value
            else:
                process_descriptions(value)
    elif isinstance(content, list):
        for item in content:
            process_descriptions(item)

def collect_openapi_components(FILE_PATHS, EXCLUDED_TAGS):
    collected_data = {
        "paths": {},
        "schemas": {},
        "securitySchemes": {},
        "tags": {},
        "x-tagGroups": {}
    }

    for group_name, file_path in FILE_PATHS.items():
        if not os.path.exists(file_path):
            print(f"Skipping missing file: {file_path}")
            continue

        with open(file_path, 'r') as content_file:
            parsed_content = yaml.safe_load(content_file.read())

        process_descriptions(parsed_content)

        paths = parsed_content.get('paths', {})
        collected_data["paths"].update(paths)

        components = parsed_content.get('components', {})
        schemas = components.get('schemas', {})
        collected_data["schemas"].update(schemas)

        security_schemes = components.get('securitySchemes', {})
        collected_data["securitySchemes"].update(security_schemes)

        tags = parsed_content.get('tags', [])
        for tag in tags:
            if group_name in EXCLUDED_TAGS and tag['name'] in EXCLUDED_TAGS[group_name]:
                continue

            original_tag_name = tag['name']
            display_name = transform_tag_name(original_tag_name)
            tag['x-displayName'] = display_name
            collected_data["tags"][original_tag_name] = tag

            group_name_transformed = transform_tag_group_name(group_name)
            if group_name_transformed not in collected_data["x-tagGroups"]:
                collected_data["x-tagGroups"][group_name_transformed] = {"name": group_name_transformed, "tags": []}

            if original_tag_name not in collected_data["x-tagGroups"][group_name_transformed]["tags"]:
                collected_data["x-tagGroups"][group_name_transformed]["tags"].append(original_tag_name)

    return collected_data

def merge_openapi_components(collected_data):
    # Checking for no conflicts
    symbol_table = {
        "schemas": set(),
        "securitySchemes": set()
    }

    openapi_merged = {
        "openapi": "3.0.3",
        "info": {
            "title": "API Reference",
            "description": "Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples."
        },
        "paths": collected_data["paths"],
        "components": {
            "schemas": {},
            "securitySchemes": {}
        },
        "security": [],
        "tags": [],
        "x-tagGroups": []
    }

    # Add schemas and check for conflicts
    for schema_name, schema_content in collected_data["schemas"].items():
        print(schema_name)
        print(schema_content)
        if schema_name in symbol_table["schemas"]:
            raise ValueError(f"Conflicting schema name detected: {schema_name}")
        symbol_table["schemas"].add(schema_name)
        openapi_merged["components"]["schemas"][schema_name] = schema_content

    # Add security schemes and check for conflicts
    for scheme_name, scheme_content in collected_data["securitySchemes"].items():
        if scheme_name in symbol_table["securitySchemes"]:
            raise ValueError(f"Conflicting security scheme name detected: {scheme_name}")
        symbol_table["securitySchemes"].add(scheme_name)
        openapi_merged["components"]["securitySchemes"][scheme_name] = scheme_content

    openapi_merged["tags"].extend(collected_data["tags"].values())
    openapi_merged["x-tagGroups"].extend(collected_data["x-tagGroups"].values())

    return openapi_merged

collected_data = collect_openapi_components(FILE_PATHS, EXCLUDED_TAGS)
openapi_combined = merge_openapi_components(collected_data)

merged_yaml_path = 'master_api_combined.yaml'
with open(merged_yaml_path, 'w') as yaml_file:
    yaml.dump(openapi_combined, yaml_file, sort_keys=False)

print(f"Merged OpenAPI YAML saved to {merged_yaml_path}")

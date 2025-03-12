import yaml
import re
import os

# Paths to the API spec files to combine
DA_FILE_PATHS = {
    "skills_intelligence": "../res/skills-intelligence-engine.yaml",
    "compensation_benchmarks": "../res/compensation-benchmarks.yaml",
}
LEGACY_FILE_PATHS = {
    "authentication": "../res/authentication-apis.yaml",
    "data_in": "../res/data-in-apis.yaml",
    "data_out": "../res/data-out-apis.yaml",
    "administration": "../res/administration-apis.yaml",
    "analytic_model": "../res/analytic-model-apis.yaml",
    **DA_FILE_PATHS
}
FILE_PATHS = {
    "visier-apis": "../res/visier-apis.yaml",
    **DA_FILE_PATHS
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
        collected_data["schemas"][group_name] = schemas

        security_schemes = components.get('securitySchemes', {})
        collected_data["securitySchemes"][group_name] = security_schemes

        tags = parsed_content.get('tags', [])
        tag_groups = parsed_content.get('x-tagGroups', [])
        for tag in tags:

            if group_name in EXCLUDED_TAGS and tag['name'] in EXCLUDED_TAGS[group_name]:
                continue

            original_tag_name = tag['name']
            display_name = transform_tag_name(original_tag_name)
            tag['x-displayName'] = display_name
            collected_data["tags"][original_tag_name] = tag

            group_name_transformed = [tg['name'] for tg in tag_groups if original_tag_name in tg['tags']][0] if tag_groups else transform_tag_group_name(group_name)
            if group_name_transformed not in collected_data["x-tagGroups"]:
                collected_data["x-tagGroups"][group_name_transformed] = {"name": group_name_transformed, "tags": []}

            if original_tag_name not in collected_data["x-tagGroups"][group_name_transformed]["tags"]:
                collected_data["x-tagGroups"][group_name_transformed]["tags"].append(original_tag_name)

    return collected_data


def merge_elements(collected_data: dict, element_name: str) -> dict:
    """
    Merge and flag issues in the particular key in collected_data
    :param collected_data: A dictionary of the elements from each file that contributes to the combined OAS3, separated by "group" - created in collect_openapi_components()
    :return: Dictionary with combined element
    """
    elements_by_name_and_group = {}
    for group, elements in collected_data[element_name].items():
        for element, content in elements.items():
            elements_by_name_and_group[element] = elements_by_name_and_group.get(element, {})
            elements_by_name_and_group[element][group] = content

    merged_elements = {}
    problematic_elements = {}
    for element, content in elements_by_name_and_group.items():

        # Determine distinct contents
        values = list(content.values())
        matches = [z[0] == z[1] for z in zip(values, values[1:])]

        if all(matches):
            merged_elements[element] = values[0]
        else:
            msg = [f" * {group}: {c}" for group, c in content.items()]
            problematic_elements[element] = "\n".join(msg)

    if problematic_elements:
        msg = [f"{element}:\n{contents}" for element, contents in problematic_elements.items()]
        raise ValueError(f"{len(msg)} conflicting {element_name} entries:\n" + "\n".join(msg))

    return merged_elements


def merge_openapi_components(collected_data):

    openapi_merged = {
        "openapi": "3.0.3",
        "info": {
            "title": "API Reference",
            "description": "Detailed API reference documentation for Visier APIs. Includes all endpoints, headers, path parameters, query parameters, request body schema, response schema, JSON request samples, and JSON response samples."
        },
        "paths": collected_data["paths"],
        "components": {
            "schemas": merge_elements(collected_data, "schemas"),
            "securitySchemes": merge_elements(collected_data, "securitySchemes"),
        },
        "security": [],
        "tags": [],
        "x-tagGroups": []
    }

    openapi_merged["tags"].extend(collected_data["tags"].values())
    openapi_merged["x-tagGroups"].extend(collected_data["x-tagGroups"].values())

    return openapi_merged


if __name__ == '__main__':

    combine_sets = {
        'master_api_combined.yaml': FILE_PATHS,
        'master_api_combined_legacy.yaml': LEGACY_FILE_PATHS,
    }

    for merged_yaml_path, file_paths in combine_sets.items():
        collected_data = collect_openapi_components(file_paths, EXCLUDED_TAGS)
        openapi_combined = merge_openapi_components(collected_data)

        with open(merged_yaml_path, 'w') as yaml_file:
            yaml.dump(openapi_combined, yaml_file, sort_keys=False)

        print(f"Merged OpenAPI YAML saved to {merged_yaml_path}")

import yaml
from combine_yamls import (
    transform_tag_name,
    transform_tag_group_name,
    replace_br_tags,
    escape_ampersands,
    process_descriptions,
    collect_openapi_components,
    merge_openapi_components,
)

# Sample YAML content for testing
SAMPLE_YAML_CONTENT = """
paths:
  /some/path:
    get:
      summary: Some summary
      description: Some description with <br> tags
      tags:
        - SomeTag
components:
  schemas:
    SomeSchema:
      type: object
      properties:
        someProperty:
          type: string
  securitySchemes:
    SomeSecurityScheme:
      type: apiKey
      in: header
      name: X-API-Key
tags:
  - name: SomeTag
    description: Some tag description with & unescaped
"""


def test_transform_tag_name():
    assert transform_tag_name("SomeTagName") == "Some Tag Name"
    assert transform_tag_name("AnotherTagName") == "Another Tag Name"


def test_transform_tag_group_name():
    assert transform_tag_group_name("some_group") == "some group"
    assert transform_tag_group_name("another_group") == "another group"


def test_replace_br_tags():
    assert replace_br_tags("Some text with <br> tags") == "Some text with <br/> tags"
    assert replace_br_tags("Some text without br tags") == "Some text without br tags"


def test_escape_ampersands():
    assert escape_ampersands("Some text with & unescaped") == "Some text with &amp; unescaped"
    assert escape_ampersands("Some text with &amp; escaped") == "Some text with &amp; escaped"
    assert escape_ampersands("Some text with &lt; &gt; &quot; &apos;") == "Some text with &lt; &gt; &quot; &apos;"


def test_process_descriptions():
    data = yaml.safe_load(SAMPLE_YAML_CONTENT)
    process_descriptions(data)
    assert data["paths"]["/some/path"]["get"]["description"] == "Some description with <br/> tags"
    assert data["tags"][0]["description"] == "Some tag description with &amp; unescaped"


def test_collect_openapi_components():
    # Create a temporary YAML file for testing
    with open("temp_test.yaml", "w") as f:
        f.write(SAMPLE_YAML_CONTENT)

    file_paths = {"test_group": "temp_test.yaml"}
    excluded_tags = {}
    collected_data = collect_openapi_components(file_paths, excluded_tags)

    assert "/some/path" in collected_data["paths"]
    assert "SomeSchema" in collected_data["schemas"]
    assert "SomeSecurityScheme" in collected_data["securitySchemes"]
    assert "SomeTag" in collected_data["tags"]

    # Clean up the temporary file
    import os
    os.remove("temp_test.yaml")


def test_merge_openapi_components():
    collected_data = {
        "paths": {"/some/path": {"get": {"summary": "Some summary"}}},
        "schemas": {"SomeSchema": {"type": "object"}},
        "securitySchemes": {"SomeSecurityScheme": {"type": "apiKey"}},
        "tags": {"SomeTag": {"name": "SomeTag"}},
        "x-tagGroups": {"Test Group": {"name": "Test Group", "tags": ["SomeTag"]}},
    }
    merged_data = merge_openapi_components(collected_data)
    assert merged_data["openapi"] == "3.0.3"
    assert merged_data["paths"] == collected_data["paths"]
    assert merged_data["components"]["schemas"] == collected_data["schemas"]
    assert merged_data["components"]["securitySchemes"] == collected_data["securitySchemes"]
    assert merged_data["tags"] == list(collected_data["tags"].values())
    assert merged_data["x-tagGroups"] == list(collected_data["x-tagGroups"].values())
import unittest
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


class CombineYamlTests(unittest.TestCase):

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

    def test_transform_tag_name(self):
        assert transform_tag_name("SomeTagName") == "Some Tag Name"
        assert transform_tag_name("AnotherTagName") == "Another Tag Name"

    def test_transform_tag_group_name(self):
        assert transform_tag_group_name("some_group") == "some group"
        assert transform_tag_group_name("another_group") == "another group"

    def test_replace_br_tags(self):
        assert replace_br_tags("Some text with <br> tags") == "Some text with <br/> tags"
        assert replace_br_tags("Some text without br tags") == "Some text without br tags"

    def test_escape_ampersands(self):
        assert escape_ampersands("Some text with & unescaped") == "Some text with &amp; unescaped"
        assert escape_ampersands("Some text with &amp; escaped") == "Some text with &amp; escaped"
        assert escape_ampersands("Some text with &lt; &gt; &quot; &apos;") == "Some text with &lt; &gt; &quot; &apos;"

    def test_process_descriptions(self):
        data = yaml.safe_load(self.SAMPLE_YAML_CONTENT)
        process_descriptions(data)
        assert data["paths"]["/some/path"]["get"]["description"] == "Some description with <br/> tags"
        assert data["tags"][0]["description"] == "Some tag description with &amp; unescaped"

    def test_collect_openapi_components(self):
        # Create a temporary YAML file for testing
        with open("temp_test.yaml", "w") as f:
            f.write(self.SAMPLE_YAML_CONTENT)

        group_name = "test_group"

        file_paths = {group_name: "temp_test.yaml"}
        excluded_tags = {}
        collected_data = collect_openapi_components(file_paths, excluded_tags)

        assert "/some/path" in collected_data["paths"]
        assert "SomeSchema" in collected_data["schemas"][group_name]
        assert "SomeSecurityScheme" in collected_data["securitySchemes"][group_name]
        assert "SomeTag" in collected_data["tags"]

        # Clean up the temporary file
        import os
        os.remove("temp_test.yaml")

    def test_merge_openapi_components(self):
        collected_data = {
            "paths": {"/some/path": {"get": {"summary": "Some summary"}}},
            "schemas": {"test_group": {"SomeSchema": {"type": "object"}}},
            "securitySchemes": {"test_group": {"SomeSecurityScheme": {"type": "apiKey"}}},
            "tags": {"SomeTag": {"name": "SomeTag"}},
            "x-tagGroups": {"Test Group": {"name": "Test Group", "tags": ["SomeTag"]}},
        }
        merged_data = merge_openapi_components(collected_data)
        assert merged_data["openapi"] == "3.0.3"
        assert merged_data["paths"] == collected_data["paths"]
        assert merged_data["components"]["schemas"] == collected_data["schemas"]["test_group"]
        assert merged_data["components"]["securitySchemes"] == collected_data["securitySchemes"]["test_group"]
        assert merged_data["tags"] == list(collected_data["tags"].values())
        assert merged_data["x-tagGroups"] == list(collected_data["x-tagGroups"].values())

    def test_merge_openapi_components_multi_group(self):
        """ Test for schemas and security schemes with multiple declarations of the same object that match in definition resolves correctly """
        collected_data = {
            "paths": {"/some/path": {"get": {"summary": "Some summary"}}},
            "schemas": {
                "test_group": {
                    "SomeSchema": {"type": "object"}
                },
                "test_group_2": {
                    "SomeSchema": {"type": "object"}
                },
                "test_group_3": {
                    "SomeSchema": {"type": "object"},
                    "OtherSchema": {"type": "object"}
                },
            },
            "securitySchemes": {
                "test_group": {
                    "SomeSecurityScheme": {"type": "apiKey"}
                },
                "test_group_2": {
                    "SomeSecurityScheme": {"type": "apiKey"}
                },
                "test_group_3": {
                    "SomeSecurityScheme": {"type": "apiKey"},
                    "OtherSecurityScheme": {"type": "apiKey"}
                },
            },
            "tags": {"SomeTag": {"name": "SomeTag"}},
            "x-tagGroups": {"Test Group": {"name": "Test Group", "tags": ["SomeTag"]}},
        }
        merged_data = merge_openapi_components(collected_data)
        assert merged_data["openapi"] == "3.0.3"
        assert merged_data["paths"] == collected_data["paths"]
        assert merged_data["components"]["schemas"] == collected_data["schemas"]["test_group_3"]
        assert merged_data["components"]["securitySchemes"] == collected_data["securitySchemes"]["test_group_3"]
        assert merged_data["tags"] == list(collected_data["tags"].values())
        assert merged_data["x-tagGroups"] == list(collected_data["x-tagGroups"].values())

    def test_merge_openapi_components_schema_conflict(self):
        """ Test to ensure inconsistent schemas in different groups is detected """
        collected_data = {
            "paths": {"/some/path": {"get": {"summary": "Some summary"}}},
            "schemas": {
                "test_group": {"SomeSchema": {"type": "object"}},
                "test_group_2": {"SomeSchema": {"type": "string"}},
            },
            "securitySchemes": {
                "test_group": {"SomeSecurityScheme": {"type": "apiKey"}},
                "test_group_2": {"SomeSecurityScheme": {"type": "apiKey"}},
            },
            "tags": {"SomeTag": {"name": "SomeTag"}},
            "x-tagGroups": {"Test Group": {"name": "Test Group", "tags": ["SomeTag"]}},
        }
        with self.assertRaises(ValueError):
            merge_openapi_components(collected_data)

    def test_merge_openapi_components_securitySchemes_conflict(self):
        """ Test to ensure inconsistent security schemes in different groups is detected """
        collected_data = {
            "paths": {"/some/path": {"get": {"summary": "Some summary"}}},
            "schemas": {
                "test_group": {"SomeSchema": {"type": "object"}},
                "test_group_2": {"SomeSchema": {"type": "object"}},
            },
            "securitySchemes": {
                "test_group": {"SomeSecurityScheme": {"type": "apiKey"}},
                "test_group_2": {"SomeSecurityScheme": {"type": "usernamePassword"}},
            },
            "tags": {"SomeTag": {"name": "SomeTag"}},
            "x-tagGroups": {"Test Group": {"name": "Test Group", "tags": ["SomeTag"]}},
        }
        with self.assertRaises(ValueError):
            merge_openapi_components(collected_data)


if __name__ == '__main__':
    unittest.main()

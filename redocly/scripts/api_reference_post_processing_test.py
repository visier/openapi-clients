# This contains logic to post-process the API reference generated by redocly prior to pushing to our documentation team
import difflib
import unittest
from api_reference_post_processing import correct_br_tags, script_tag_adjustments, strip_html_comments, strip_version


class PostProcessingTests(unittest.TestCase):

    def test_correct_br_tags(self):

        # Basics
        assert correct_br_tags("<br>blah blah") == "<br/>blah blah"
        assert correct_br_tags("blah <br> blah") == "blah <br/> blah"
        assert correct_br_tags("blah blah <br>") == "blah blah <br/>"

        # Don't convert already properly terminated br tags
        assert correct_br_tags("<br/>") == "<br/>"

    def test_script_tag_adjustments(self):

        # script tags with no content are ignored
        snippet = expected = "<script></script>"
        result = script_tag_adjustments(snippet)
        assert result == expected, self.show_difference(expected, result)

        # script tags with attributes, but no content should also be ignored
        snippet = expected = '<script src="text/javascript"></script>'
        result = script_tag_adjustments(snippet)
        assert result == expected, self.show_difference(expected, result)

        # No content definition extends to whitespace
        snippet = expected = """<script>
        </script>"""
        result = script_tag_adjustments(snippet)
        assert result == expected, self.show_difference(expected, result)

        # Complex case with multiple script tags of varying types
        snippet = """<script src="../../Resources/Scripts/redoc-script.js"></script>
<script>
// Ensure the script is executed after the DOM is fully loaded
window.addEventListener('load', function () {
    const loadingScreen = document.getElementById('loading-screen');
if (loadingScreen) {
    loadingScreen.classList.add('hidden');
}
});
</script>
<script src="https://cdn.redocly.com/redoc/v2.4.0/bundles/redoc.standalone.js"></script>"""
        expected = """<script src="../../Resources/Scripts/redoc-script.js"></script>
<script>
//<![CDATA[
// Ensure the script is executed after the DOM is fully loaded
window.addEventListener('load', function () {
    const loadingScreen = document.getElementById('loading-screen');
if (loadingScreen) {
    loadingScreen.classList.add('hidden');
}
});
//]]>
</script>
<script src="https://cdn.redocly.com/redoc/v2.4.0/bundles/redoc.standalone.js"></script>"""
        result = script_tag_adjustments(snippet)
        assert result == expected, self.show_difference(expected, result)

    def test_strip_html_comments(self):

        # Empty comments
        assert strip_html_comments("<!-- -->") == ""

        snippet = """Foo
        <!-- -->
        Bar"""
        expected = """Foo
        Bar"""
        result = strip_html_comments(snippet)
        assert result == expected, self.show_difference(expected, result)

        # Leave comments with content alone!
        snippet = expected = "<!-- some comment in HTML -->"
        result = strip_html_comments(snippet)
        assert result == expected, self.show_difference(expected, result)

    def test_strip_version(self):

        # Version strings inside a span tag, wrapped in round brackets, should get dropped
        assert strip_version("<span>(12345678.12345.12345)</span>") == ""

        # Version strings in the JSON should get dropped
        assert strip_version(',"version":"12345678.12345.12345"') == ""

        # Version strings not in a span tag should be OK
        assert strip_version("12345678.12345.12345") == "12345678.12345.12345"

    @staticmethod
    def show_difference(expected, result):
        return "\n".join(difflib.unified_diff(expected.splitlines(),
                                              result.splitlines(),
                                              fromfile="expected",
                                              tofile="result",
                                              lineterm=""
                                              )
                         )


if __name__ == '__main__':
    unittest.main()
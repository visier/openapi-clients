from visier.model_query import ApiClient, rest

from samples.python.model_query_usage import refresh_api_key


class CustomApiClient(ApiClient):
    """Custom API client for implementing refresh token logic."""

    def call_api(
            self,
            method,
            url,
            header_params=None,
            body=None,
            post_params=None,
            _request_timeout=None
    ) -> rest.RESTResponse:
        refresh_api_key(self.configuration)
        return super().call_api(method, url, header_params, body, post_params, _request_timeout)

# coding: utf-8

"""
    Visier Data Intake APIs

    Visier APIs for sending raw or untransformed source data to Visier

    The version of the OpenAPI document: 22222222.99201.1389
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from visier.api.data_intake.api.data_intake_api import DataIntakeApi


class TestDataIntakeApi(unittest.TestCase):
    """DataIntakeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DataIntakeApi()

    def tearDown(self) -> None:
        pass

    def test_get_processing_jobs_by_parent_receiving_job_id(self) -> None:
        """Test case for get_processing_jobs_by_parent_receiving_job_id

        Retrieve processing job statuses by receiving job ID
        """
        pass

    def test_get_sources(self) -> None:
        """Test case for get_sources

        Retrieve a list of sources
        """
        pass

    def test_push_data(self) -> None:
        """Test case for push_data

        Transfer data to sources via JSON
        """
        pass

    def test_push_data_cancel(self) -> None:
        """Test case for push_data_cancel

        Cancel a transfer session
        """
        pass

    def test_push_data_complete(self) -> None:
        """Test case for push_data_complete

        Complete a transfer session
        """
        pass

    def test_receiving_job_status(self) -> None:
        """Test case for receiving_job_status

        Retrieve a receiving job’s status
        """
        pass

    def test_start_transfer(self) -> None:
        """Test case for start_transfer

        Start a transfer session
        """
        pass

    def test_upload_data(self) -> None:
        """Test case for upload_data

        Transfer data to sources via file upload
        """
        pass


if __name__ == '__main__':
    unittest.main()

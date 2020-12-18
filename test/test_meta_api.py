# coding: utf-8

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import cda_client
from cda_client.api.meta_api import MetaApi  # noqa: E501
from cda_client.rest import ApiException


class TestMetaApi(unittest.TestCase):
    """MetaApi unit test stubs"""

    def setUp(self):
        self.api = cda_client.api.meta_api.MetaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_release_notes(self):
        """Test case for all_release_notes

        List descriptions of all available datasets  # noqa: E501
        """
        pass

    def test_latest_release_notes(self):
        """Test case for latest_release_notes

        Description of latest dataset  # noqa: E501
        """
        pass

    def test_service_status(self):
        """Test case for service_status

        CDA status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

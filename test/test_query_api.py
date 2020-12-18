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
from cda_client.api.query_api import QueryApi  # noqa: E501
from cda_client.rest import ApiException


class TestQueryApi(unittest.TestCase):
    """QueryApi unit test stubs"""

    def setUp(self):
        self.api = cda_client.api.query_api.QueryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_boolean_query(self):
        """Test case for boolean_query

        Execute boolean query  # noqa: E501
        """
        pass

    def test_bulk_data(self):
        """Test case for bulk_data

        Return all data in CDA  # noqa: E501
        """
        pass

    def test_ping(self):
        """Test case for ping

        """
        pass

    def test_sql_query(self):
        """Test case for sql_query

        Execute SQL directly on a version of the dataset  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import cda_client
from cda_client.model.dataset_info import DatasetInfo
from cda_client.model.model import Model
globals()['DatasetInfo'] = DatasetInfo
globals()['Model'] = Model
from cda_client.model.dataset_description import DatasetDescription


class TestDatasetDescription(unittest.TestCase):
    """DatasetDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatasetDescription(self):
        """Test DatasetDescription"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DatasetDescription()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

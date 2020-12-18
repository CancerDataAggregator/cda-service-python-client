# coding: utf-8

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import cda_client
from cda_client.models.dataset_description import DatasetDescription  # noqa: E501
from cda_client.rest import ApiException

class TestDatasetDescription(unittest.TestCase):
    """DatasetDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DatasetDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = cda_client.models.dataset_description.DatasetDescription()  # noqa: E501
        if include_optional :
            return DatasetDescription(
                release_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                cda_version = '0', 
                cda_model = cda_client.models.model.Model(
                    version = '0', 
                    date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    model = cda_client.models.model.model(), ), 
                notes = '0', 
                datasets = [
                    cda_client.models.dataset_info.DatasetInfo(
                        source = '0', 
                        version = '0', 
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else :
            return DatasetDescription(
        )

    def testDatasetDescription(self):
        """Test DatasetDescription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

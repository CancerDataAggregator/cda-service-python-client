# coding: utf-8

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cda_client.configuration import Configuration


class QueryResponseData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'result': 'list[object]',
        'query_sql': 'str',
        'total_row_count': 'int',
        'next_url': 'str'
    }

    attribute_map = {
        'result': 'result',
        'query_sql': 'query_sql',
        'total_row_count': 'total_row_count',
        'next_url': 'next_url'
    }

    def __init__(self, result=None, query_sql=None, total_row_count=None, next_url=None, local_vars_configuration=None):  # noqa: E501
        """QueryResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._result = None
        self._query_sql = None
        self._total_row_count = None
        self._next_url = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if query_sql is not None:
            self.query_sql = query_sql
        self.total_row_count = total_row_count
        self.next_url = next_url

    @property
    def result(self):
        """Gets the result of this QueryResponseData.  # noqa: E501


        :return: The result of this QueryResponseData.  # noqa: E501
        :rtype: list[object]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QueryResponseData.


        :param result: The result of this QueryResponseData.  # noqa: E501
        :type result: list[object]
        """

        self._result = result

    @property
    def query_sql(self):
        """Gets the query_sql of this QueryResponseData.  # noqa: E501

        the generated BigQuery SQL  # noqa: E501

        :return: The query_sql of this QueryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._query_sql

    @query_sql.setter
    def query_sql(self, query_sql):
        """Sets the query_sql of this QueryResponseData.

        the generated BigQuery SQL  # noqa: E501

        :param query_sql: The query_sql of this QueryResponseData.  # noqa: E501
        :type query_sql: str
        """

        self._query_sql = query_sql

    @property
    def total_row_count(self):
        """Gets the total_row_count of this QueryResponseData.  # noqa: E501

        the total number of rows in the query. can be null if the query is not complete  # noqa: E501

        :return: The total_row_count of this QueryResponseData.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this QueryResponseData.

        the total number of rows in the query. can be null if the query is not complete  # noqa: E501

        :param total_row_count: The total_row_count of this QueryResponseData.  # noqa: E501
        :type total_row_count: int
        """

        self._total_row_count = total_row_count

    @property
    def next_url(self):
        """Gets the next_url of this QueryResponseData.  # noqa: E501

        a URL to use to fetch the next page of data in the query. can be null if the query is not complete  # noqa: E501

        :return: The next_url of this QueryResponseData.  # noqa: E501
        :rtype: str
        """
        return self._next_url

    @next_url.setter
    def next_url(self, next_url):
        """Sets the next_url of this QueryResponseData.

        a URL to use to fetch the next page of data in the query. can be null if the query is not complete  # noqa: E501

        :param next_url: The next_url of this QueryResponseData.  # noqa: E501
        :type next_url: str
        """

        self._next_url = next_url

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryResponseData):
            return True

        return self.to_dict() != other.to_dict()

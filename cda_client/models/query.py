# coding: utf-8

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 1.0.0-rc.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cda_client.configuration import Configuration


class Query(object):
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
        'node_type': 'str',
        'value': 'str',
        'l': 'Query',
        'r': 'Query'
    }

    attribute_map = {
        'node_type': 'node_type',
        'value': 'value',
        'l': 'l',
        'r': 'r'
    }

    def __init__(self, node_type=None, value=None, l=None, r=None, local_vars_configuration=None):  # noqa: E501
        """Query - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._node_type = None
        self._value = None
        self._l = None
        self._r = None
        self.discriminator = None

        if node_type is not None:
            self.node_type = node_type
        if value is not None:
            self.value = value
        if l is not None:
            self.l = l
        if r is not None:
            self.r = r

    @property
    def node_type(self):
        """Gets the node_type of this Query.  # noqa: E501


        :return: The node_type of this Query.  # noqa: E501
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this Query.


        :param node_type: The node_type of this Query.  # noqa: E501
        :type: str
        """
        allowed_values = ["column", "quoted", "unquoted", ">=", "<=", "<", ">", "=", "~", "AND", "OR", "NOT", "LIMIT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and node_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"  # noqa: E501
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def value(self):
        """Gets the value of this Query.  # noqa: E501


        :return: The value of this Query.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Query.


        :param value: The value of this Query.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def l(self):
        """Gets the l of this Query.  # noqa: E501


        :return: The l of this Query.  # noqa: E501
        :rtype: Query
        """
        return self._l

    @l.setter
    def l(self, l):
        """Sets the l of this Query.


        :param l: The l of this Query.  # noqa: E501
        :type: Query
        """

        self._l = l

    @property
    def r(self):
        """Gets the r of this Query.  # noqa: E501


        :return: The r of this Query.  # noqa: E501
        :rtype: Query
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this Query.


        :param r: The r of this Query.  # noqa: E501
        :type: Query
        """

        self._r = r

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Query):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Query):
            return True

        return self.to_dict() != other.to_dict()

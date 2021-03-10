# coding: utf-8

"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cda_client.configuration import Configuration


class SystemStatus(object):
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
        'ok': 'bool',
        'systems': 'dict(str, SystemStatusSystems)'
    }

    attribute_map = {
        'ok': 'ok',
        'systems': 'systems'
    }

    def __init__(self, ok=None, systems=None, local_vars_configuration=None):  # noqa: E501
        """SystemStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ok = None
        self._systems = None
        self.discriminator = None

        if ok is not None:
            self.ok = ok
        if systems is not None:
            self.systems = systems

    @property
    def ok(self):
        """Gets the ok of this SystemStatus.  # noqa: E501

        status of this service  # noqa: E501

        :return: The ok of this SystemStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this SystemStatus.

        status of this service  # noqa: E501

        :param ok: The ok of this SystemStatus.  # noqa: E501
        :type: bool
        """

        self._ok = ok

    @property
    def systems(self):
        """Gets the systems of this SystemStatus.  # noqa: E501


        :return: The systems of this SystemStatus.  # noqa: E501
        :rtype: dict(str, SystemStatusSystems)
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this SystemStatus.


        :param systems: The systems of this SystemStatus.  # noqa: E501
        :type: dict(str, SystemStatusSystems)
        """

        self._systems = systems

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
        if not isinstance(other, SystemStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemStatus):
            return True

        return self.to_dict() != other.to_dict()

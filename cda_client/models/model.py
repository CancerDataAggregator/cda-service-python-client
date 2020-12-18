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


class Model(object):
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
        'version': 'str',
        'date': 'datetime',
        'model': 'object'
    }

    attribute_map = {
        'version': 'version',
        'date': 'date',
        'model': 'model'
    }

    def __init__(self, version=None, date=None, model=None, local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._date = None
        self._model = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if date is not None:
            self.date = date
        if model is not None:
            self.model = model

    @property
    def version(self):
        """Gets the version of this Model.  # noqa: E501


        :return: The version of this Model.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Model.


        :param version: The version of this Model.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def date(self):
        """Gets the date of this Model.  # noqa: E501


        :return: The date of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Model.


        :param date: The date of this Model.  # noqa: E501
        :type: datetime
        """

        self._date = date

    @property
    def model(self):
        """Gets the model of this Model.  # noqa: E501


        :return: The model of this Model.  # noqa: E501
        :rtype: object
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Model.


        :param model: The model of this Model.  # noqa: E501
        :type: object
        """

        self._model = model

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
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()

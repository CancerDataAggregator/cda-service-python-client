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


class DatasetInfo(object):
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
        'source': 'str',
        'version': 'str',
        'date': 'str'
    }

    attribute_map = {
        'source': 'source',
        'version': 'version',
        'date': 'date'
    }

    def __init__(self, source=None, version=None, date=None, local_vars_configuration=None):  # noqa: E501
        """DatasetInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._source = None
        self._version = None
        self._date = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if version is not None:
            self.version = version
        if date is not None:
            self.date = date

    @property
    def source(self):
        """Gets the source of this DatasetInfo.  # noqa: E501


        :return: The source of this DatasetInfo.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DatasetInfo.


        :param source: The source of this DatasetInfo.  # noqa: E501
        :type source: str
        """

        self._source = source

    @property
    def version(self):
        """Gets the version of this DatasetInfo.  # noqa: E501


        :return: The version of this DatasetInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatasetInfo.


        :param version: The version of this DatasetInfo.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def date(self):
        """Gets the date of this DatasetInfo.  # noqa: E501


        :return: The date of this DatasetInfo.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DatasetInfo.


        :param date: The date of this DatasetInfo.  # noqa: E501
        :type date: str
        """

        self._date = date

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
        if not isinstance(other, DatasetInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetInfo):
            return True

        return self.to_dict() != other.to_dict()

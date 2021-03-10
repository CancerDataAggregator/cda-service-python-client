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


class DatasetDescription(object):
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
        'release_date': 'datetime',
        'cda_version': 'str',
        'cda_model': 'Model',
        'notes': 'str',
        'datasets': 'list[DatasetInfo]'
    }

    attribute_map = {
        'release_date': 'release-date',
        'cda_version': 'cda-version',
        'cda_model': 'cda-model',
        'notes': 'notes',
        'datasets': 'datasets'
    }

    def __init__(self, release_date=None, cda_version=None, cda_model=None, notes=None, datasets=None, local_vars_configuration=None):  # noqa: E501
        """DatasetDescription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._release_date = None
        self._cda_version = None
        self._cda_model = None
        self._notes = None
        self._datasets = None
        self.discriminator = None

        if release_date is not None:
            self.release_date = release_date
        if cda_version is not None:
            self.cda_version = cda_version
        if cda_model is not None:
            self.cda_model = cda_model
        if notes is not None:
            self.notes = notes
        if datasets is not None:
            self.datasets = datasets

    @property
    def release_date(self):
        """Gets the release_date of this DatasetDescription.  # noqa: E501


        :return: The release_date of this DatasetDescription.  # noqa: E501
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this DatasetDescription.


        :param release_date: The release_date of this DatasetDescription.  # noqa: E501
        :type: datetime
        """

        self._release_date = release_date

    @property
    def cda_version(self):
        """Gets the cda_version of this DatasetDescription.  # noqa: E501


        :return: The cda_version of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._cda_version

    @cda_version.setter
    def cda_version(self, cda_version):
        """Sets the cda_version of this DatasetDescription.


        :param cda_version: The cda_version of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._cda_version = cda_version

    @property
    def cda_model(self):
        """Gets the cda_model of this DatasetDescription.  # noqa: E501


        :return: The cda_model of this DatasetDescription.  # noqa: E501
        :rtype: Model
        """
        return self._cda_model

    @cda_model.setter
    def cda_model(self, cda_model):
        """Sets the cda_model of this DatasetDescription.


        :param cda_model: The cda_model of this DatasetDescription.  # noqa: E501
        :type: Model
        """

        self._cda_model = cda_model

    @property
    def notes(self):
        """Gets the notes of this DatasetDescription.  # noqa: E501


        :return: The notes of this DatasetDescription.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this DatasetDescription.


        :param notes: The notes of this DatasetDescription.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def datasets(self):
        """Gets the datasets of this DatasetDescription.  # noqa: E501


        :return: The datasets of this DatasetDescription.  # noqa: E501
        :rtype: list[DatasetInfo]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this DatasetDescription.


        :param datasets: The datasets of this DatasetDescription.  # noqa: E501
        :type: list[DatasetInfo]
        """

        self._datasets = datasets

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
        if not isinstance(other, DatasetDescription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetDescription):
            return True

        return self.to_dict() != other.to_dict()

# coding: utf-8

"""
    Waitlisted API

    Waitlisted API

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ReservationsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, uuid=None, email=None, affiliate=None, name=None, referred_count=None, position=None, total_count=None, activated_at=None, created_at=None):
        """
        ReservationsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'uuid': 'str',
            'email': 'str',
            'affiliate': 'str',
            'name': 'str',
            'referred_count': 'int',
            'position': 'int',
            'total_count': 'int',
            'activated_at': 'datetime',
            'created_at': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'uuid': 'uuid',
            'email': 'email',
            'affiliate': 'affiliate',
            'name': 'name',
            'referred_count': 'referred_count',
            'position': 'position',
            'total_count': 'total_count',
            'activated_at': 'activated_at',
            'created_at': 'created_at'
        }

        self._id = id
        self._uuid = uuid
        self._email = email
        self._affiliate = affiliate
        self._name = name
        self._referred_count = referred_count
        self._position = position
        self._total_count = total_count
        self._activated_at = activated_at
        self._created_at = created_at

    @property
    def id(self):
        """
        Gets the id of this ReservationsResponse.


        :return: The id of this ReservationsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReservationsResponse.


        :param id: The id of this ReservationsResponse.
        :type: str
        """

        self._id = id

    @property
    def uuid(self):
        """
        Gets the uuid of this ReservationsResponse.


        :return: The uuid of this ReservationsResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this ReservationsResponse.


        :param uuid: The uuid of this ReservationsResponse.
        :type: str
        """

        self._uuid = uuid

    @property
    def email(self):
        """
        Gets the email of this ReservationsResponse.


        :return: The email of this ReservationsResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this ReservationsResponse.


        :param email: The email of this ReservationsResponse.
        :type: str
        """

        self._email = email

    @property
    def affiliate(self):
        """
        Gets the affiliate of this ReservationsResponse.


        :return: The affiliate of this ReservationsResponse.
        :rtype: str
        """
        return self._affiliate

    @affiliate.setter
    def affiliate(self, affiliate):
        """
        Sets the affiliate of this ReservationsResponse.


        :param affiliate: The affiliate of this ReservationsResponse.
        :type: str
        """

        self._affiliate = affiliate

    @property
    def name(self):
        """
        Gets the name of this ReservationsResponse.


        :return: The name of this ReservationsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReservationsResponse.


        :param name: The name of this ReservationsResponse.
        :type: str
        """

        self._name = name

    @property
    def referred_count(self):
        """
        Gets the referred_count of this ReservationsResponse.


        :return: The referred_count of this ReservationsResponse.
        :rtype: int
        """
        return self._referred_count

    @referred_count.setter
    def referred_count(self, referred_count):
        """
        Sets the referred_count of this ReservationsResponse.


        :param referred_count: The referred_count of this ReservationsResponse.
        :type: int
        """

        self._referred_count = referred_count

    @property
    def position(self):
        """
        Gets the position of this ReservationsResponse.


        :return: The position of this ReservationsResponse.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ReservationsResponse.


        :param position: The position of this ReservationsResponse.
        :type: int
        """

        self._position = position

    @property
    def total_count(self):
        """
        Gets the total_count of this ReservationsResponse.


        :return: The total_count of this ReservationsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this ReservationsResponse.


        :param total_count: The total_count of this ReservationsResponse.
        :type: int
        """

        self._total_count = total_count

    @property
    def activated_at(self):
        """
        Gets the activated_at of this ReservationsResponse.


        :return: The activated_at of this ReservationsResponse.
        :rtype: datetime
        """
        return self._activated_at

    @activated_at.setter
    def activated_at(self, activated_at):
        """
        Sets the activated_at of this ReservationsResponse.


        :param activated_at: The activated_at of this ReservationsResponse.
        :type: datetime
        """

        self._activated_at = activated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this ReservationsResponse.


        :return: The created_at of this ReservationsResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ReservationsResponse.


        :param created_at: The created_at of this ReservationsResponse.
        :type: datetime
        """

        self._created_at = created_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
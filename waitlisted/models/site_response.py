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


class SiteResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, brand_color=None, button_text_color=None, custom_styles=None, ask_name=None, signup_title=None, signup_copy=None, position_title=None, social_copy=None, social_message=None, domain=None, share_social_copy=None, referral_copy=None, check_position_copy=None, join_button_copy=None, check_reservation_copy=None, email_field_label=None, name_field_label=None, thank_you_share_template=None, waitlist_threshold=None, use_custom_thank_you=None, hide_waitlist=None, unmet_shared_template=None, threshold_met=None, website_url=None, tracking_code=None, custom_css=None, hide_branding=None, total_count=None):
        """
        SiteResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'brand_color': 'str',
            'button_text_color': 'str',
            'custom_styles': 'str',
            'ask_name': 'bool',
            'signup_title': 'str',
            'signup_copy': 'str',
            'position_title': 'str',
            'social_copy': 'str',
            'social_message': 'str',
            'domain': 'str',
            'share_social_copy': 'str',
            'referral_copy': 'str',
            'check_position_copy': 'str',
            'join_button_copy': 'str',
            'check_reservation_copy': 'str',
            'email_field_label': 'str',
            'name_field_label': 'str',
            'thank_you_share_template': 'str',
            'waitlist_threshold': 'int',
            'use_custom_thank_you': 'bool',
            'hide_waitlist': 'bool',
            'unmet_shared_template': 'str',
            'threshold_met': 'bool',
            'website_url': 'str',
            'tracking_code': 'str',
            'custom_css': 'str',
            'hide_branding': 'bool',
            'total_count': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'brand_color': 'brand_color',
            'button_text_color': 'button_text_color',
            'custom_styles': 'custom_styles',
            'ask_name': 'ask_name',
            'signup_title': 'signup_title',
            'signup_copy': 'signup_copy',
            'position_title': 'position_title',
            'social_copy': 'social_copy',
            'social_message': 'social_message',
            'domain': 'domain',
            'share_social_copy': 'share_social_copy',
            'referral_copy': 'referral_copy',
            'check_position_copy': 'check_position_copy',
            'join_button_copy': 'join_button_copy',
            'check_reservation_copy': 'check_reservation_copy',
            'email_field_label': 'email_field_label',
            'name_field_label': 'name_field_label',
            'thank_you_share_template': 'thank_you_share_template',
            'waitlist_threshold': 'waitlist_threshold',
            'use_custom_thank_you': 'use_custom_thank_you',
            'hide_waitlist': 'hide_waitlist',
            'unmet_shared_template': 'unmet_shared_template',
            'threshold_met': 'threshold_met',
            'website_url': 'website_url',
            'tracking_code': 'tracking_code',
            'custom_css': 'custom_css',
            'hide_branding': 'hide_branding',
            'total_count': 'total_count'
        }

        self._id = id
        self._brand_color = brand_color
        self._button_text_color = button_text_color
        self._custom_styles = custom_styles
        self._ask_name = ask_name
        self._signup_title = signup_title
        self._signup_copy = signup_copy
        self._position_title = position_title
        self._social_copy = social_copy
        self._social_message = social_message
        self._domain = domain
        self._share_social_copy = share_social_copy
        self._referral_copy = referral_copy
        self._check_position_copy = check_position_copy
        self._join_button_copy = join_button_copy
        self._check_reservation_copy = check_reservation_copy
        self._email_field_label = email_field_label
        self._name_field_label = name_field_label
        self._thank_you_share_template = thank_you_share_template
        self._waitlist_threshold = waitlist_threshold
        self._use_custom_thank_you = use_custom_thank_you
        self._hide_waitlist = hide_waitlist
        self._unmet_shared_template = unmet_shared_template
        self._threshold_met = threshold_met
        self._website_url = website_url
        self._tracking_code = tracking_code
        self._custom_css = custom_css
        self._hide_branding = hide_branding
        self._total_count = total_count

    @property
    def id(self):
        """
        Gets the id of this SiteResponse.


        :return: The id of this SiteResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SiteResponse.


        :param id: The id of this SiteResponse.
        :type: str
        """

        self._id = id

    @property
    def brand_color(self):
        """
        Gets the brand_color of this SiteResponse.


        :return: The brand_color of this SiteResponse.
        :rtype: str
        """
        return self._brand_color

    @brand_color.setter
    def brand_color(self, brand_color):
        """
        Sets the brand_color of this SiteResponse.


        :param brand_color: The brand_color of this SiteResponse.
        :type: str
        """

        self._brand_color = brand_color

    @property
    def button_text_color(self):
        """
        Gets the button_text_color of this SiteResponse.


        :return: The button_text_color of this SiteResponse.
        :rtype: str
        """
        return self._button_text_color

    @button_text_color.setter
    def button_text_color(self, button_text_color):
        """
        Sets the button_text_color of this SiteResponse.


        :param button_text_color: The button_text_color of this SiteResponse.
        :type: str
        """

        self._button_text_color = button_text_color

    @property
    def custom_styles(self):
        """
        Gets the custom_styles of this SiteResponse.


        :return: The custom_styles of this SiteResponse.
        :rtype: str
        """
        return self._custom_styles

    @custom_styles.setter
    def custom_styles(self, custom_styles):
        """
        Sets the custom_styles of this SiteResponse.


        :param custom_styles: The custom_styles of this SiteResponse.
        :type: str
        """

        self._custom_styles = custom_styles

    @property
    def ask_name(self):
        """
        Gets the ask_name of this SiteResponse.


        :return: The ask_name of this SiteResponse.
        :rtype: bool
        """
        return self._ask_name

    @ask_name.setter
    def ask_name(self, ask_name):
        """
        Sets the ask_name of this SiteResponse.


        :param ask_name: The ask_name of this SiteResponse.
        :type: bool
        """

        self._ask_name = ask_name

    @property
    def signup_title(self):
        """
        Gets the signup_title of this SiteResponse.


        :return: The signup_title of this SiteResponse.
        :rtype: str
        """
        return self._signup_title

    @signup_title.setter
    def signup_title(self, signup_title):
        """
        Sets the signup_title of this SiteResponse.


        :param signup_title: The signup_title of this SiteResponse.
        :type: str
        """

        self._signup_title = signup_title

    @property
    def signup_copy(self):
        """
        Gets the signup_copy of this SiteResponse.


        :return: The signup_copy of this SiteResponse.
        :rtype: str
        """
        return self._signup_copy

    @signup_copy.setter
    def signup_copy(self, signup_copy):
        """
        Sets the signup_copy of this SiteResponse.


        :param signup_copy: The signup_copy of this SiteResponse.
        :type: str
        """

        self._signup_copy = signup_copy

    @property
    def position_title(self):
        """
        Gets the position_title of this SiteResponse.


        :return: The position_title of this SiteResponse.
        :rtype: str
        """
        return self._position_title

    @position_title.setter
    def position_title(self, position_title):
        """
        Sets the position_title of this SiteResponse.


        :param position_title: The position_title of this SiteResponse.
        :type: str
        """

        self._position_title = position_title

    @property
    def social_copy(self):
        """
        Gets the social_copy of this SiteResponse.


        :return: The social_copy of this SiteResponse.
        :rtype: str
        """
        return self._social_copy

    @social_copy.setter
    def social_copy(self, social_copy):
        """
        Sets the social_copy of this SiteResponse.


        :param social_copy: The social_copy of this SiteResponse.
        :type: str
        """

        self._social_copy = social_copy

    @property
    def social_message(self):
        """
        Gets the social_message of this SiteResponse.


        :return: The social_message of this SiteResponse.
        :rtype: str
        """
        return self._social_message

    @social_message.setter
    def social_message(self, social_message):
        """
        Sets the social_message of this SiteResponse.


        :param social_message: The social_message of this SiteResponse.
        :type: str
        """

        self._social_message = social_message

    @property
    def domain(self):
        """
        Gets the domain of this SiteResponse.


        :return: The domain of this SiteResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this SiteResponse.


        :param domain: The domain of this SiteResponse.
        :type: str
        """

        self._domain = domain

    @property
    def share_social_copy(self):
        """
        Gets the share_social_copy of this SiteResponse.


        :return: The share_social_copy of this SiteResponse.
        :rtype: str
        """
        return self._share_social_copy

    @share_social_copy.setter
    def share_social_copy(self, share_social_copy):
        """
        Sets the share_social_copy of this SiteResponse.


        :param share_social_copy: The share_social_copy of this SiteResponse.
        :type: str
        """

        self._share_social_copy = share_social_copy

    @property
    def referral_copy(self):
        """
        Gets the referral_copy of this SiteResponse.


        :return: The referral_copy of this SiteResponse.
        :rtype: str
        """
        return self._referral_copy

    @referral_copy.setter
    def referral_copy(self, referral_copy):
        """
        Sets the referral_copy of this SiteResponse.


        :param referral_copy: The referral_copy of this SiteResponse.
        :type: str
        """

        self._referral_copy = referral_copy

    @property
    def check_position_copy(self):
        """
        Gets the check_position_copy of this SiteResponse.


        :return: The check_position_copy of this SiteResponse.
        :rtype: str
        """
        return self._check_position_copy

    @check_position_copy.setter
    def check_position_copy(self, check_position_copy):
        """
        Sets the check_position_copy of this SiteResponse.


        :param check_position_copy: The check_position_copy of this SiteResponse.
        :type: str
        """

        self._check_position_copy = check_position_copy

    @property
    def join_button_copy(self):
        """
        Gets the join_button_copy of this SiteResponse.


        :return: The join_button_copy of this SiteResponse.
        :rtype: str
        """
        return self._join_button_copy

    @join_button_copy.setter
    def join_button_copy(self, join_button_copy):
        """
        Sets the join_button_copy of this SiteResponse.


        :param join_button_copy: The join_button_copy of this SiteResponse.
        :type: str
        """

        self._join_button_copy = join_button_copy

    @property
    def check_reservation_copy(self):
        """
        Gets the check_reservation_copy of this SiteResponse.


        :return: The check_reservation_copy of this SiteResponse.
        :rtype: str
        """
        return self._check_reservation_copy

    @check_reservation_copy.setter
    def check_reservation_copy(self, check_reservation_copy):
        """
        Sets the check_reservation_copy of this SiteResponse.


        :param check_reservation_copy: The check_reservation_copy of this SiteResponse.
        :type: str
        """

        self._check_reservation_copy = check_reservation_copy

    @property
    def email_field_label(self):
        """
        Gets the email_field_label of this SiteResponse.


        :return: The email_field_label of this SiteResponse.
        :rtype: str
        """
        return self._email_field_label

    @email_field_label.setter
    def email_field_label(self, email_field_label):
        """
        Sets the email_field_label of this SiteResponse.


        :param email_field_label: The email_field_label of this SiteResponse.
        :type: str
        """

        self._email_field_label = email_field_label

    @property
    def name_field_label(self):
        """
        Gets the name_field_label of this SiteResponse.


        :return: The name_field_label of this SiteResponse.
        :rtype: str
        """
        return self._name_field_label

    @name_field_label.setter
    def name_field_label(self, name_field_label):
        """
        Sets the name_field_label of this SiteResponse.


        :param name_field_label: The name_field_label of this SiteResponse.
        :type: str
        """

        self._name_field_label = name_field_label

    @property
    def thank_you_share_template(self):
        """
        Gets the thank_you_share_template of this SiteResponse.


        :return: The thank_you_share_template of this SiteResponse.
        :rtype: str
        """
        return self._thank_you_share_template

    @thank_you_share_template.setter
    def thank_you_share_template(self, thank_you_share_template):
        """
        Sets the thank_you_share_template of this SiteResponse.


        :param thank_you_share_template: The thank_you_share_template of this SiteResponse.
        :type: str
        """

        self._thank_you_share_template = thank_you_share_template

    @property
    def waitlist_threshold(self):
        """
        Gets the waitlist_threshold of this SiteResponse.


        :return: The waitlist_threshold of this SiteResponse.
        :rtype: int
        """
        return self._waitlist_threshold

    @waitlist_threshold.setter
    def waitlist_threshold(self, waitlist_threshold):
        """
        Sets the waitlist_threshold of this SiteResponse.


        :param waitlist_threshold: The waitlist_threshold of this SiteResponse.
        :type: int
        """

        self._waitlist_threshold = waitlist_threshold

    @property
    def use_custom_thank_you(self):
        """
        Gets the use_custom_thank_you of this SiteResponse.


        :return: The use_custom_thank_you of this SiteResponse.
        :rtype: bool
        """
        return self._use_custom_thank_you

    @use_custom_thank_you.setter
    def use_custom_thank_you(self, use_custom_thank_you):
        """
        Sets the use_custom_thank_you of this SiteResponse.


        :param use_custom_thank_you: The use_custom_thank_you of this SiteResponse.
        :type: bool
        """

        self._use_custom_thank_you = use_custom_thank_you

    @property
    def hide_waitlist(self):
        """
        Gets the hide_waitlist of this SiteResponse.


        :return: The hide_waitlist of this SiteResponse.
        :rtype: bool
        """
        return self._hide_waitlist

    @hide_waitlist.setter
    def hide_waitlist(self, hide_waitlist):
        """
        Sets the hide_waitlist of this SiteResponse.


        :param hide_waitlist: The hide_waitlist of this SiteResponse.
        :type: bool
        """

        self._hide_waitlist = hide_waitlist

    @property
    def unmet_shared_template(self):
        """
        Gets the unmet_shared_template of this SiteResponse.


        :return: The unmet_shared_template of this SiteResponse.
        :rtype: str
        """
        return self._unmet_shared_template

    @unmet_shared_template.setter
    def unmet_shared_template(self, unmet_shared_template):
        """
        Sets the unmet_shared_template of this SiteResponse.


        :param unmet_shared_template: The unmet_shared_template of this SiteResponse.
        :type: str
        """

        self._unmet_shared_template = unmet_shared_template

    @property
    def threshold_met(self):
        """
        Gets the threshold_met of this SiteResponse.


        :return: The threshold_met of this SiteResponse.
        :rtype: bool
        """
        return self._threshold_met

    @threshold_met.setter
    def threshold_met(self, threshold_met):
        """
        Sets the threshold_met of this SiteResponse.


        :param threshold_met: The threshold_met of this SiteResponse.
        :type: bool
        """

        self._threshold_met = threshold_met

    @property
    def website_url(self):
        """
        Gets the website_url of this SiteResponse.


        :return: The website_url of this SiteResponse.
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, website_url):
        """
        Sets the website_url of this SiteResponse.


        :param website_url: The website_url of this SiteResponse.
        :type: str
        """

        self._website_url = website_url

    @property
    def tracking_code(self):
        """
        Gets the tracking_code of this SiteResponse.


        :return: The tracking_code of this SiteResponse.
        :rtype: str
        """
        return self._tracking_code

    @tracking_code.setter
    def tracking_code(self, tracking_code):
        """
        Sets the tracking_code of this SiteResponse.


        :param tracking_code: The tracking_code of this SiteResponse.
        :type: str
        """

        self._tracking_code = tracking_code

    @property
    def custom_css(self):
        """
        Gets the custom_css of this SiteResponse.


        :return: The custom_css of this SiteResponse.
        :rtype: str
        """
        return self._custom_css

    @custom_css.setter
    def custom_css(self, custom_css):
        """
        Sets the custom_css of this SiteResponse.


        :param custom_css: The custom_css of this SiteResponse.
        :type: str
        """

        self._custom_css = custom_css

    @property
    def hide_branding(self):
        """
        Gets the hide_branding of this SiteResponse.


        :return: The hide_branding of this SiteResponse.
        :rtype: bool
        """
        return self._hide_branding

    @hide_branding.setter
    def hide_branding(self, hide_branding):
        """
        Sets the hide_branding of this SiteResponse.


        :param hide_branding: The hide_branding of this SiteResponse.
        :type: bool
        """

        self._hide_branding = hide_branding

    @property
    def total_count(self):
        """
        Gets the total_count of this SiteResponse.


        :return: The total_count of this SiteResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this SiteResponse.


        :param total_count: The total_count of this SiteResponse.
        :type: int
        """

        self._total_count = total_count

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

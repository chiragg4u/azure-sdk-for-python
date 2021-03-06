# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .user_base_py3 import UserBase


class UserUpdateParameters(UserBase):
    """Request parameters for updating an existing work or school account user.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param immutable_id: This must be specified if you are using a federated
     domain for the user's userPrincipalName (UPN) property when creating a new
     user account. It is used to associate an on-premises Active Directory user
     account with their Azure AD user object.
    :type immutable_id: str
    :param usage_location: A two letter country code (ISO standard 3166).
     Required for users that will be assigned licenses due to legal requirement
     to check for availability of services in countries. Examples include:
     "US", "JP", and "GB".
    :type usage_location: str
    :param given_name: The given name for the user.
    :type given_name: str
    :param surname: The user's surname (family name or last name).
    :type surname: str
    :param user_type: A string value that can be used to classify user types
     in your directory, such as 'Member' and 'Guest'. Possible values include:
     'Member', 'Guest'
    :type user_type: str or ~azure.graphrbac.models.UserType
    :param account_enabled: Whether the account is enabled.
    :type account_enabled: bool
    :param display_name: The display name of the user.
    :type display_name: str
    :param password_profile: The password profile of the user.
    :type password_profile: ~azure.graphrbac.models.PasswordProfile
    :param user_principal_name: The user principal name
     (someuser@contoso.com). It must contain one of the verified domains for
     the tenant.
    :type user_principal_name: str
    :param mail_nickname: The mail alias for the user.
    :type mail_nickname: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'immutable_id': {'key': 'immutableId', 'type': 'str'},
        'usage_location': {'key': 'usageLocation', 'type': 'str'},
        'given_name': {'key': 'givenName', 'type': 'str'},
        'surname': {'key': 'surname', 'type': 'str'},
        'user_type': {'key': 'userType', 'type': 'str'},
        'account_enabled': {'key': 'accountEnabled', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'password_profile': {'key': 'passwordProfile', 'type': 'PasswordProfile'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, immutable_id: str=None, usage_location: str=None, given_name: str=None, surname: str=None, user_type=None, account_enabled: bool=None, display_name: str=None, password_profile=None, user_principal_name: str=None, mail_nickname: str=None, **kwargs) -> None:
        super(UserUpdateParameters, self).__init__(additional_properties=additional_properties, immutable_id=immutable_id, usage_location=usage_location, given_name=given_name, surname=surname, user_type=user_type, **kwargs)
        self.account_enabled = account_enabled
        self.display_name = display_name
        self.password_profile = password_profile
        self.user_principal_name = user_principal_name
        self.mail_nickname = mail_nickname

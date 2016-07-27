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

from msrest.serialization import Model


class HostNameSslState(Model):
    """Object that represents a SSL-enabled host name.

    :param name: Host name
    :type name: str
    :param ssl_state: SSL type. Possible values include: 'Disabled',
     'SniEnabled', 'IpBasedEnabled'
    :type ssl_state: str or :class:`SslState <azure.mgmt.web.models.SslState>`
    :param virtual_ip: Virtual IP address assigned to the host name if IP
     based SSL is enabled
    :type virtual_ip: str
    :param thumbprint: SSL cert thumbprint
    :type thumbprint: str
    :param to_update: Set this flag to update existing host name
    :type to_update: bool
    """ 

    _validation = {
        'ssl_state': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'ssl_state': {'key': 'sslState', 'type': 'SslState'},
        'virtual_ip': {'key': 'virtualIP', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'to_update': {'key': 'toUpdate', 'type': 'bool'},
    }

    def __init__(self, ssl_state, name=None, virtual_ip=None, thumbprint=None, to_update=None):
        self.name = name
        self.ssl_state = ssl_state
        self.virtual_ip = virtual_ip
        self.thumbprint = thumbprint
        self.to_update = to_update
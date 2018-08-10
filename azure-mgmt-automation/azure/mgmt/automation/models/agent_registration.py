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


class AgentRegistration(Model):
    """Definition of the agent registration infomration type.

    :param dsc_meta_configuration: Gets or sets the dsc meta configuration.
    :type dsc_meta_configuration: str
    :param endpoint: Gets or sets the dsc server endpoint.
    :type endpoint: str
    :param keys: Gets or sets the agent registration keys.
    :type keys: ~azure.mgmt.automation.models.AgentRegistrationKeys
    :param id: Gets or sets the id.
    :type id: str
    """

    _attribute_map = {
        'dsc_meta_configuration': {'key': 'dscMetaConfiguration', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'keys': {'key': 'keys', 'type': 'AgentRegistrationKeys'},
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AgentRegistration, self).__init__(**kwargs)
        self.dsc_meta_configuration = kwargs.get('dsc_meta_configuration', None)
        self.endpoint = kwargs.get('endpoint', None)
        self.keys = kwargs.get('keys', None)
        self.id = kwargs.get('id', None)

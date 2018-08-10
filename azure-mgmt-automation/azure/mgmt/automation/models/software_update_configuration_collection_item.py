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


class SoftwareUpdateConfigurationCollectionItem(Model):
    """Software update configuration collection item properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the software update configuration.
    :vartype name: str
    :ivar id: Resource Id of the software update configuration
    :vartype id: str
    :param update_configuration: Update specific properties of the software
     update configuration.
    :type update_configuration:
     ~azure.mgmt.automation.models.CollectionItemUpdateConfiguration
    :param frequency: execution frequency of the schedule associated with the
     software update configuration. Possible values include: 'OneTime', 'Day',
     'Hour', 'Week', 'Month'
    :type frequency: str or ~azure.mgmt.automation.models.ScheduleFrequency
    :param start_time: the start time of the update.
    :type start_time: datetime
    :ivar creation_time: Creation time of the software update configuration,
     which only appears in the response.
    :vartype creation_time: datetime
    :ivar last_modified_time: Last time software update configuration was
     modified, which only appears in the response.
    :vartype last_modified_time: datetime
    :ivar provisioning_state: Provisioning state for the software update
     configuration, which only appears in the response.
    :vartype provisioning_state: str
    :param next_run: ext run time of the update.
    :type next_run: datetime
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'update_configuration': {'key': 'properties.updateConfiguration', 'type': 'CollectionItemUpdateConfiguration'},
        'frequency': {'key': 'properties.frequency', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'next_run': {'key': 'properties.nextRun', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(SoftwareUpdateConfigurationCollectionItem, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.update_configuration = kwargs.get('update_configuration', None)
        self.frequency = kwargs.get('frequency', None)
        self.start_time = kwargs.get('start_time', None)
        self.creation_time = None
        self.last_modified_time = None
        self.provisioning_state = None
        self.next_run = kwargs.get('next_run', None)

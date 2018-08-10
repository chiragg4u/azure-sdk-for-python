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

from .tracked_resource import TrackedResource


class Runbook(TrackedResource):
    """Definition of the runbook type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param runbook_type: Gets or sets the type of the runbook. Possible values
     include: 'Script', 'Graph', 'PowerShellWorkflow', 'PowerShell',
     'GraphPowerShellWorkflow', 'GraphPowerShell'
    :type runbook_type: str or ~azure.mgmt.automation.models.RunbookTypeEnum
    :param publish_content_link: Gets or sets the published runbook content
     link.
    :type publish_content_link: ~azure.mgmt.automation.models.ContentLink
    :param state: Gets or sets the state of the runbook. Possible values
     include: 'New', 'Edit', 'Published'
    :type state: str or ~azure.mgmt.automation.models.RunbookState
    :param log_verbose: Gets or sets verbose log option.
    :type log_verbose: bool
    :param log_progress: Gets or sets progress log option.
    :type log_progress: bool
    :param log_activity_trace: Gets or sets the option to log activity trace
     of the runbook.
    :type log_activity_trace: int
    :param job_count: Gets or sets the job count of the runbook.
    :type job_count: int
    :param parameters: Gets or sets the runbook parameters.
    :type parameters: dict[str,
     ~azure.mgmt.automation.models.RunbookParameter]
    :param output_types: Gets or sets the runbook output types.
    :type output_types: list[str]
    :param draft: Gets or sets the draft runbook properties.
    :type draft: ~azure.mgmt.automation.models.RunbookDraft
    :param provisioning_state: Gets or sets the provisioning state of the
     runbook. Possible values include: 'Succeeded'
    :type provisioning_state: str or
     ~azure.mgmt.automation.models.RunbookProvisioningState
    :param last_modified_by: Gets or sets the last modified by.
    :type last_modified_by: str
    :param creation_time: Gets or sets the creation time.
    :type creation_time: datetime
    :param last_modified_time: Gets or sets the last modified time.
    :type last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'runbook_type': {'key': 'properties.runbookType', 'type': 'str'},
        'publish_content_link': {'key': 'properties.publishContentLink', 'type': 'ContentLink'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'log_verbose': {'key': 'properties.logVerbose', 'type': 'bool'},
        'log_progress': {'key': 'properties.logProgress', 'type': 'bool'},
        'log_activity_trace': {'key': 'properties.logActivityTrace', 'type': 'int'},
        'job_count': {'key': 'properties.jobCount', 'type': 'int'},
        'parameters': {'key': 'properties.parameters', 'type': '{RunbookParameter}'},
        'output_types': {'key': 'properties.outputTypes', 'type': '[str]'},
        'draft': {'key': 'properties.draft', 'type': 'RunbookDraft'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'RunbookProvisioningState'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Runbook, self).__init__(**kwargs)
        self.runbook_type = kwargs.get('runbook_type', None)
        self.publish_content_link = kwargs.get('publish_content_link', None)
        self.state = kwargs.get('state', None)
        self.log_verbose = kwargs.get('log_verbose', None)
        self.log_progress = kwargs.get('log_progress', None)
        self.log_activity_trace = kwargs.get('log_activity_trace', None)
        self.job_count = kwargs.get('job_count', None)
        self.parameters = kwargs.get('parameters', None)
        self.output_types = kwargs.get('output_types', None)
        self.draft = kwargs.get('draft', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.creation_time = kwargs.get('creation_time', None)
        self.last_modified_time = kwargs.get('last_modified_time', None)
        self.description = kwargs.get('description', None)
        self.etag = kwargs.get('etag', None)

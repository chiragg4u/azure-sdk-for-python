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

from .update_resource import UpdateResource


class DtlEnvironmentFragment(UpdateResource):
    """An environment, which is essentially an ARM template deployment.

    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param deployment_properties: The deployment properties of the
     environment.
    :type deployment_properties:
     ~azure.mgmt.devtestlabs.models.EnvironmentDeploymentPropertiesFragment
    :param arm_template_display_name: The display name of the Azure Resource
     Manager template that produced the environment.
    :type arm_template_display_name: str
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'deployment_properties': {'key': 'properties.deploymentProperties', 'type': 'EnvironmentDeploymentPropertiesFragment'},
        'arm_template_display_name': {'key': 'properties.armTemplateDisplayName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DtlEnvironmentFragment, self).__init__(**kwargs)
        self.deployment_properties = kwargs.get('deployment_properties', None)
        self.arm_template_display_name = kwargs.get('arm_template_display_name', None)

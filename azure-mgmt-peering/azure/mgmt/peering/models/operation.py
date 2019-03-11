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


class Operation(Model):
    """The peering API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation.
    :vartype name: str
    :ivar display: The information related to the operation.
    :vartype display: ~azure.mgmt.peering.models.OperationDisplayInfo
    :ivar is_data_action: The flag that indicates whether the operation
     applies to data plane.
    :vartype is_data_action: bool
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
        'is_data_action': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayInfo'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None
        self.is_data_action = None
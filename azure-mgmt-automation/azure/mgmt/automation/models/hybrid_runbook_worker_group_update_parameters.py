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


class HybridRunbookWorkerGroupUpdateParameters(Model):
    """Parameters supplied to the update operation.

    :param credential: Sets the credential of a worker group.
    :type credential:
     ~azure.mgmt.automation.models.RunAsCredentialAssociationProperty
    """

    _attribute_map = {
        'credential': {'key': 'credential', 'type': 'RunAsCredentialAssociationProperty'},
    }

    def __init__(self, **kwargs):
        super(HybridRunbookWorkerGroupUpdateParameters, self).__init__(**kwargs)
        self.credential = kwargs.get('credential', None)

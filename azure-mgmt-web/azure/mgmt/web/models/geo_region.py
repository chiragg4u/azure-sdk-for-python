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

from .resource import Resource


class GeoRegion(Resource):
    """Geographical region.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param geo_region_name: Region name
    :type geo_region_name: str
    :param description: Region description
    :type description: str
    :param display_name: Display name for region
    :type display_name: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'geo_region_name': {'key': 'properties.name', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, geo_region_name=None, description=None, display_name=None):
        super(GeoRegion, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.geo_region_name = geo_region_name
        self.description = description
        self.display_name = display_name
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

from .search_results_answer import SearchResultsAnswer


class Videos(SearchResultsAnswer):
    """Defines a video answer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param _type: Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar web_search_url: The URL To Bing's search result for this item.
    :vartype web_search_url: str
    :ivar follow_up_queries:
    :vartype follow_up_queries:
     list[~azure.cognitiveservices.search.videosearch.models.Query]
    :ivar total_estimated_matches: The estimated number of webpages that are
     relevant to the query. Use this number along with the count and offset
     query parameters to page the results.
    :vartype total_estimated_matches: long
    :ivar is_family_friendly:
    :vartype is_family_friendly: bool
    :param value: A list of video objects that are relevant to the query.
    :type value:
     list[~azure.cognitiveservices.search.videosearch.models.VideoObject]
    :ivar next_offset:
    :vartype next_offset: int
    :ivar scenario: Possible values include: 'List', 'SingleDominantVideo'
    :vartype scenario: str or
     ~azure.cognitiveservices.search.videosearch.models.VideoQueryScenario
    :ivar query_expansions:
    :vartype query_expansions:
     list[~azure.cognitiveservices.search.videosearch.models.Query]
    :ivar pivot_suggestions:
    :vartype pivot_suggestions:
     list[~azure.cognitiveservices.search.videosearch.models.PivotSuggestions]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'web_search_url': {'readonly': True},
        'follow_up_queries': {'readonly': True},
        'total_estimated_matches': {'readonly': True},
        'is_family_friendly': {'readonly': True},
        'value': {'required': True},
        'next_offset': {'readonly': True},
        'scenario': {'readonly': True},
        'query_expansions': {'readonly': True},
        'pivot_suggestions': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'follow_up_queries': {'key': 'followUpQueries', 'type': '[Query]'},
        'total_estimated_matches': {'key': 'totalEstimatedMatches', 'type': 'long'},
        'is_family_friendly': {'key': 'isFamilyFriendly', 'type': 'bool'},
        'value': {'key': 'value', 'type': '[VideoObject]'},
        'next_offset': {'key': 'nextOffset', 'type': 'int'},
        'scenario': {'key': 'scenario', 'type': 'VideoQueryScenario'},
        'query_expansions': {'key': 'queryExpansions', 'type': '[Query]'},
        'pivot_suggestions': {'key': 'pivotSuggestions', 'type': '[PivotSuggestions]'},
    }

    def __init__(self, value):
        super(Videos, self).__init__()
        self.value = value
        self.next_offset = None
        self.scenario = None
        self.query_expansions = None
        self.pivot_suggestions = None
        self._type = 'Videos'
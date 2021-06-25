"""
    CDA API

    API definition for the CDA  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cda_client.api_client import ApiClient, Endpoint as _Endpoint
from cda_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from cda_client.model.query import Query
from cda_client.model.query_created_data import QueryCreatedData
from cda_client.model.query_response_data import QueryResponseData


class QueryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __boolean_query(
            self,
            query,
            version="v3",
            **kwargs
        ):
            """Execute boolean query  # noqa: E501

            Execute a query composed of conditions on columns combined with boolean operators. The generated SQL query is returned in the response.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.boolean_query(query, version="v3", async_req=True)
            >>> result = thread.get()

            Args:
                query (Query): The boolean query
                version (str): Dataset version. defaults to "v3", must be one of ["v3"]

            Keyword Args:
                dry_run (bool): If true, don't run the query, only generate and return it.. [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryCreatedData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['version'] = \
                version
            kwargs['query'] = \
                query
            return self.call_with_http_info(**kwargs)

        self.boolean_query = _Endpoint(
            settings={
                'response_type': (QueryCreatedData,),
                'auth': [],
                'endpoint_path': '/api/v1/boolean-query/{version}',
                'operation_id': 'boolean_query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'version',
                    'query',
                    'dry_run',
                ],
                'required': [
                    'version',
                    'query',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'version':
                        (str,),
                    'query':
                        (Query,),
                    'dry_run':
                        (bool,),
                },
                'attribute_map': {
                    'version': 'version',
                    'dry_run': 'dryRun',
                },
                'location_map': {
                    'version': 'path',
                    'query': 'body',
                    'dry_run': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__boolean_query
        )

        def __bulk_data(
            self,
            version="v3",
            **kwargs
        ):
            """Return all data in CDA  # noqa: E501

            Return all data in CDA  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bulk_data(version="v3", async_req=True)
            >>> result = thread.get()

            Args:
                version (str): Dataset version. defaults to "v3", must be one of ["v3"]

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryCreatedData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['version'] = \
                version
            return self.call_with_http_info(**kwargs)

        self.bulk_data = _Endpoint(
            settings={
                'response_type': (QueryCreatedData,),
                'auth': [],
                'endpoint_path': '/api/v1/bulk-data/{version}',
                'operation_id': 'bulk_data',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'version',
                ],
                'required': [
                    'version',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'version':
                        (str,),
                },
                'attribute_map': {
                    'version': 'version',
                },
                'location_map': {
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__bulk_data
        )

        def __query(
            self,
            id,
            **kwargs
        ):
            """Given a query ID, return the a page of data from the query result.  # noqa: E501

            Use this API to get the data back from a query. If there is more data present, next_url will contain the link to use to get the rest of the data. If the current page of data is not yet ready, the result will be empty, but next_url will be set.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.query(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Query ID

            Keyword Args:
                offset (int): The number of entries to skip. [optional] if omitted the server will use the default value of 0
                limit (int): The numbers of entries to return per page of data. [optional] if omitted the server will use the default value of 1000
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryResponseData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.query = _Endpoint(
            settings={
                'response_type': (QueryResponseData,),
                'auth': [],
                'endpoint_path': '/api/v1/query/{id}',
                'operation_id': 'query',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'offset',
                    'limit',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'offset': 'offset',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'offset': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__query
        )

        def __sql_query(
            self,
            body,
            **kwargs
        ):
            """Execute SQL directly on a version of the dataset  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.sql_query(body, async_req=True)
            >>> result = thread.get()

            Args:
                body (str): BigQuery SQL to run on data table

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryCreatedData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.sql_query = _Endpoint(
            settings={
                'response_type': (QueryCreatedData,),
                'auth': [],
                'endpoint_path': '/api/v1/sql-query',
                'operation_id': 'sql_query',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'body',
                ],
                'required': [
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'body':
                        (str,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'text/plain'
                ]
            },
            api_client=api_client,
            callable=__sql_query
        )

        def __unique_values(
            self,
            body,
            version="v3",
            **kwargs
        ):
            """Returns all unique values  # noqa: E501

            Return unique values given a qualified columnName  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.unique_values(body, version="v3", async_req=True)
            >>> result = thread.get()

            Args:
                body (str): column_name of table value being requested
                version (str): Dataset version. defaults to "v3", must be one of ["v3"]

            Keyword Args:
                system (str): Filter on system for results. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                QueryCreatedData
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['version'] = \
                version
            kwargs['body'] = \
                body
            return self.call_with_http_info(**kwargs)

        self.unique_values = _Endpoint(
            settings={
                'response_type': (QueryCreatedData,),
                'auth': [],
                'endpoint_path': '/api/v1/unique-values/{version}',
                'operation_id': 'unique_values',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'version',
                    'body',
                    'system',
                ],
                'required': [
                    'version',
                    'body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'version':
                        (str,),
                    'body':
                        (str,),
                    'system':
                        (str,),
                },
                'attribute_map': {
                    'version': 'version',
                    'system': 'system',
                },
                'location_map': {
                    'version': 'path',
                    'body': 'body',
                    'system': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'text/plain'
                ]
            },
            api_client=api_client,
            callable=__unique_values
        )

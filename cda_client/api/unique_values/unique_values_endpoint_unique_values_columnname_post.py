from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.unique_value_response_obj import UniqueValueResponseObj
from ...types import UNSET, Response, Unset


def _get_kwargs(
    columnname: str,
    *,
    system: Union[Unset, str] = "",
    count: Union[Unset, bool] = False,
    total_count: Union[Unset, bool] = False,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["system"] = system

    params["count"] = count

    params["totalCount"] = total_count

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/unique_values/{columnname}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UniqueValueResponseObj]]:
    if response.status_code == 200:
        response_200 = UniqueValueResponseObj.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, UniqueValueResponseObj]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    columnname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    system: Union[Unset, str] = "",
    count: Union[Unset, bool] = False,
    total_count: Union[Unset, bool] = False,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, UniqueValueResponseObj]]:
    """Unique Values Endpoint

     _summary_

    Args:
        request (Request): _description_
        column_name (str): _description_
        qnode (QNode): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        FrequencyResponseObj: _description_

    Args:
        columnname (str):
        system (Union[Unset, str]):  Default: ''.
        count (Union[Unset, bool]):  Default: False.
        total_count (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UniqueValueResponseObj]]
    """

    kwargs = _get_kwargs(
        columnname=columnname,
        system=system,
        count=count,
        total_count=total_count,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    columnname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    system: Union[Unset, str] = "",
    count: Union[Unset, bool] = False,
    total_count: Union[Unset, bool] = False,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, UniqueValueResponseObj]]:
    """Unique Values Endpoint

     _summary_

    Args:
        request (Request): _description_
        column_name (str): _description_
        qnode (QNode): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        FrequencyResponseObj: _description_

    Args:
        columnname (str):
        system (Union[Unset, str]):  Default: ''.
        count (Union[Unset, bool]):  Default: False.
        total_count (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UniqueValueResponseObj]
    """

    return sync_detailed(
        columnname=columnname,
        client=client,
        system=system,
        count=count,
        total_count=total_count,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    columnname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    system: Union[Unset, str] = "",
    count: Union[Unset, bool] = False,
    total_count: Union[Unset, bool] = False,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[HTTPValidationError, UniqueValueResponseObj]]:
    """Unique Values Endpoint

     _summary_

    Args:
        request (Request): _description_
        column_name (str): _description_
        qnode (QNode): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        FrequencyResponseObj: _description_

    Args:
        columnname (str):
        system (Union[Unset, str]):  Default: ''.
        count (Union[Unset, bool]):  Default: False.
        total_count (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UniqueValueResponseObj]]
    """

    kwargs = _get_kwargs(
        columnname=columnname,
        system=system,
        count=count,
        total_count=total_count,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    columnname: str,
    *,
    client: Union[AuthenticatedClient, Client],
    system: Union[Unset, str] = "",
    count: Union[Unset, bool] = False,
    total_count: Union[Unset, bool] = False,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[HTTPValidationError, UniqueValueResponseObj]]:
    """Unique Values Endpoint

     _summary_

    Args:
        request (Request): _description_
        column_name (str): _description_
        qnode (QNode): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        FrequencyResponseObj: _description_

    Args:
        columnname (str):
        system (Union[Unset, str]):  Default: ''.
        count (Union[Unset, bool]):  Default: False.
        total_count (Union[Unset, bool]):  Default: False.
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UniqueValueResponseObj]
    """

    return (
        await asyncio_detailed(
            columnname=columnname,
            client=client,
            system=system,
            count=count,
            total_count=total_count,
            limit=limit,
            offset=offset,
        )
    ).parsed

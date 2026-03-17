from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_error import ClientError
from ...models.http_validation_error import HTTPValidationError
from ...models.internal_error import InternalError
from ...models.summary_request_body import SummaryRequestBody
from ...models.summary_response_obj import SummaryResponseObj
from ...types import Response


def _get_kwargs(
    *,
    body: SummaryRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/summary/file",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientError | HTTPValidationError | InternalError | SummaryResponseObj | None:
    if response.status_code == 200:
        response_200 = SummaryResponseObj.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ClientError.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = InternalError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClientError | HTTPValidationError | InternalError | SummaryResponseObj]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SummaryRequestBody,
) -> Response[ClientError | HTTPValidationError | InternalError | SummaryResponseObj]:
    """File Summary Endpoint

     _summary_

    Args:
        request (Request): _description_
        request_body (SummaryRequestBody): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        SummaryResponseObj: _description_

    Args:
        body (SummaryRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientError | HTTPValidationError | InternalError | SummaryResponseObj]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SummaryRequestBody,
) -> ClientError | HTTPValidationError | InternalError | SummaryResponseObj | None:
    """File Summary Endpoint

     _summary_

    Args:
        request (Request): _description_
        request_body (SummaryRequestBody): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        SummaryResponseObj: _description_

    Args:
        body (SummaryRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientError | HTTPValidationError | InternalError | SummaryResponseObj
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SummaryRequestBody,
) -> Response[ClientError | HTTPValidationError | InternalError | SummaryResponseObj]:
    """File Summary Endpoint

     _summary_

    Args:
        request (Request): _description_
        request_body (SummaryRequestBody): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        SummaryResponseObj: _description_

    Args:
        body (SummaryRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientError | HTTPValidationError | InternalError | SummaryResponseObj]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SummaryRequestBody,
) -> ClientError | HTTPValidationError | InternalError | SummaryResponseObj | None:
    """File Summary Endpoint

     _summary_

    Args:
        request (Request): _description_
        request_body (SummaryRequestBody): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        SummaryResponseObj: _description_

    Args:
        body (SummaryRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientError | HTTPValidationError | InternalError | SummaryResponseObj
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

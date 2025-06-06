# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.registered_script_list import RegisteredScriptList
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...errors.bad_request_error import BadRequestError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.error import Error
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.internal_server_error import InternalServerError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.custom_code_hosted_response import CustomCodeHostedResponse
from ...types.custom_code_inline_response import CustomCodeInlineResponse
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScriptsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RegisteredScriptList:
        """
        List of scripts registered to a Site.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.
        Additionally, Scripts can be remotely hosted, or registered as inline snippets.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredScriptList
            Request was successful

        Examples
        --------
        from webflow import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.list(
            site_id="580e63e98c9a982ac9b8b741",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RegisteredScriptList,
                    parse_obj_as(
                        type_=RegisteredScriptList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def register_hosted(
        self,
        site_id: str,
        *,
        hosted_location: str,
        integrity_hash: str,
        version: str,
        display_name: str,
        can_copy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeHostedResponse:
        """
        Add a script to a Site's Custom Code registry.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.
        Additionally, Scripts can be remotely hosted, or registered as inline snippets.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        hosted_location : str
            URI for an externally hosted script location

        integrity_hash : str
            Sub-Resource Integrity Hash

        version : str
            A Semantic Version (SemVer) string, denoting the version of the script

        display_name : str
            User-facing name for the script. Must be between 1 and 50 alphanumeric characters

        can_copy : typing.Optional[bool]
            Define whether the script can be copied on site duplication and transfer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomCodeHostedResponse
            Request was successful

        Examples
        --------
        from webflow import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.register_hosted(
            site_id="580e63e98c9a982ac9b8b741",
            hosted_location="hostedLocation",
            integrity_hash="integrityHash",
            version="version",
            display_name="displayName",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts/hosted",
            method="POST",
            json={
                "hostedLocation": hosted_location,
                "integrityHash": integrity_hash,
                "canCopy": can_copy,
                "version": version,
                "displayName": display_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CustomCodeHostedResponse,
                    parse_obj_as(
                        type_=CustomCodeHostedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def register_inline(
        self,
        site_id: str,
        *,
        source_code: str,
        version: str,
        display_name: str,
        integrity_hash: typing.Optional[str] = OMIT,
        can_copy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeInlineResponse:
        """
        Add a script to a Site's Custom Code registry. Inline scripts can be between 1 and 2000 characters.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        source_code : str
            The code to be added to the site (to be hosted by Webflow).

        version : str
            A Semantic Version (SemVer) string, denoting the version of the script

        display_name : str
            User-facing name for the script. Must be between 1 and 50 alphanumeric characters

        integrity_hash : typing.Optional[str]
            Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)

        can_copy : typing.Optional[bool]
            Define whether the script can be copied on site duplication and transfer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomCodeInlineResponse
            Created

        Examples
        --------
        from webflow import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.scripts.register_inline(
            site_id="580e63e98c9a982ac9b8b741",
            source_code="alert('hello world');",
            version="0.0.1",
            display_name="Alert",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts/inline",
            method="POST",
            json={
                "sourceCode": source_code,
                "integrityHash": integrity_hash,
                "canCopy": can_copy,
                "version": version,
                "displayName": display_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CustomCodeInlineResponse,
                    parse_obj_as(
                        type_=CustomCodeInlineResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScriptsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisteredScriptList:
        """
        List of scripts registered to a Site.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.
        Additionally, Scripts can be remotely hosted, or registered as inline snippets.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisteredScriptList
            Request was successful

        Examples
        --------
        import asyncio

        from webflow import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )


        async def main() -> None:
            await client.scripts.list(
                site_id="580e63e98c9a982ac9b8b741",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RegisteredScriptList,
                    parse_obj_as(
                        type_=RegisteredScriptList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def register_hosted(
        self,
        site_id: str,
        *,
        hosted_location: str,
        integrity_hash: str,
        version: str,
        display_name: str,
        can_copy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeHostedResponse:
        """
        Add a script to a Site's Custom Code registry.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.
        Additionally, Scripts can be remotely hosted, or registered as inline snippets.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        hosted_location : str
            URI for an externally hosted script location

        integrity_hash : str
            Sub-Resource Integrity Hash

        version : str
            A Semantic Version (SemVer) string, denoting the version of the script

        display_name : str
            User-facing name for the script. Must be between 1 and 50 alphanumeric characters

        can_copy : typing.Optional[bool]
            Define whether the script can be copied on site duplication and transfer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomCodeHostedResponse
            Request was successful

        Examples
        --------
        import asyncio

        from webflow import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )


        async def main() -> None:
            await client.scripts.register_hosted(
                site_id="580e63e98c9a982ac9b8b741",
                hosted_location="hostedLocation",
                integrity_hash="integrityHash",
                version="version",
                display_name="displayName",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts/hosted",
            method="POST",
            json={
                "hostedLocation": hosted_location,
                "integrityHash": integrity_hash,
                "canCopy": can_copy,
                "version": version,
                "displayName": display_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CustomCodeHostedResponse,
                    parse_obj_as(
                        type_=CustomCodeHostedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def register_inline(
        self,
        site_id: str,
        *,
        source_code: str,
        version: str,
        display_name: str,
        integrity_hash: typing.Optional[str] = OMIT,
        can_copy: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CustomCodeInlineResponse:
        """
        Add a script to a Site's Custom Code registry. Inline scripts can be between 1 and 2000 characters.

        In order to use the Custom Code APIs for Sites and Pages, Custom Code Scripts must first be registered
        to a Site via the `registered_scripts` endpoints, and then applied to a Site or Page using the appropriate
        `custom_code` endpoints.

        <Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

        Required scope | `custom_code:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        source_code : str
            The code to be added to the site (to be hosted by Webflow).

        version : str
            A Semantic Version (SemVer) string, denoting the version of the script

        display_name : str
            User-facing name for the script. Must be between 1 and 50 alphanumeric characters

        integrity_hash : typing.Optional[str]
            Sub-Resource Integrity Hash. Only required for externally hosted scripts (passed via hostedLocation)

        can_copy : typing.Optional[bool]
            Define whether the script can be copied on site duplication and transfer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CustomCodeInlineResponse
            Created

        Examples
        --------
        import asyncio

        from webflow import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )


        async def main() -> None:
            await client.scripts.register_inline(
                site_id="580e63e98c9a982ac9b8b741",
                source_code="alert('hello world');",
                version="0.0.1",
                display_name="Alert",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{jsonable_encoder(site_id)}/registered_scripts/inline",
            method="POST",
            json={
                "sourceCode": source_code,
                "integrityHash": integrity_hash,
                "canCopy": can_copy,
                "version": version,
                "displayName": display_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CustomCodeInlineResponse,
                    parse_obj_as(
                        type_=CustomCodeInlineResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

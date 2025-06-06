# This file was auto-generated by Fern from our API Definition.

from webflow import Webflow
from webflow import AsyncWebflow
import typing
from ..utilities import validate_response
from webflow import ScriptApply


async def test_get_custom_code(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "scripts": [
            {
                "id": "cms_slider",
                "location": "header",
                "version": "1.0.0",
                "attributes": {"my-attribute": "some-value"},
            },
            {"id": "alert", "location": "header", "version": "0.0.1", "attributes": {"key": "value"}},
        ],
        "lastUpdated": "2022-10-26T00:28:54.191Z",
        "createdOn": "2022-10-26T00:28:54.191Z",
    }
    expected_types: typing.Any = {
        "scripts": (
            "list",
            {
                0: {"id": None, "location": None, "version": None, "attributes": ("dict", {0: (None, None)})},
                1: {"id": None, "location": None, "version": None, "attributes": ("dict", {0: (None, None)})},
            },
        ),
        "lastUpdated": None,
        "createdOn": None,
    }
    response = client.sites.scripts.get_custom_code(site_id="580e63e98c9a982ac9b8b741")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.sites.scripts.get_custom_code(site_id="580e63e98c9a982ac9b8b741")
    validate_response(async_response, expected_response, expected_types)


async def test_upsert_custom_code(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "scripts": [
            {
                "id": "cms_slider",
                "location": "header",
                "version": "1.0.0",
                "attributes": {"my-attribute": "some-value"},
            },
            {"id": "alert", "location": "header", "version": "0.0.1", "attributes": {"key": "value"}},
        ],
        "lastUpdated": "lastUpdated",
        "createdOn": "createdOn",
    }
    expected_types: typing.Any = {
        "scripts": (
            "list",
            {
                0: {"id": None, "location": None, "version": None, "attributes": ("dict", {0: (None, None)})},
                1: {"id": None, "location": None, "version": None, "attributes": ("dict", {0: (None, None)})},
            },
        ),
        "lastUpdated": None,
        "createdOn": None,
    }
    response = client.sites.scripts.upsert_custom_code(
        site_id="580e63e98c9a982ac9b8b741",
        scripts=[
            ScriptApply(id="cms_slider", location="header", version="1.0.0", attributes={"my-attribute": "some-value"}),
            ScriptApply(id="alert", location="header", version="0.0.1"),
        ],
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.sites.scripts.upsert_custom_code(
        site_id="580e63e98c9a982ac9b8b741",
        scripts=[
            ScriptApply(id="cms_slider", location="header", version="1.0.0", attributes={"my-attribute": "some-value"}),
            ScriptApply(id="alert", location="header", version="0.0.1"),
        ],
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_custom_code(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.sites.scripts.delete_custom_code(site_id="580e63e98c9a982ac9b8b741")  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.sites.scripts.delete_custom_code(site_id="580e63e98c9a982ac9b8b741")  # type: ignore[func-returns-value]
        is None
    )


async def test_list_custom_code_blocks(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "blocks": [
            {
                "siteId": "6258612d1ee792848f805dcf",
                "pageId": "pageId",
                "type": "site",
                "scripts": [
                    {"id": "chartjs", "location": "header", "version": "4.4.2", "attributes": {"key": "value"}}
                ],
                "createdOn": "2024-04-03T16:49:15Z",
                "lastUpdated": "2024-04-03T16:49:15Z",
            },
            {
                "siteId": "6390c49674a71f84b51a08d8",
                "pageId": "6419db964a9c43f6a3af6348",
                "type": "page",
                "scripts": [{"id": "id", "location": "header", "version": "version"}],
                "createdOn": "2022-10-26T00:28:54Z",
                "lastUpdated": "2022-10-26T00:28:54Z",
            },
        ],
        "pagination": {"limit": 10, "offset": 0, "total": 1},
    }
    expected_types: typing.Any = {
        "blocks": (
            "list",
            {
                0: {
                    "siteId": None,
                    "pageId": None,
                    "type": None,
                    "scripts": (
                        "list",
                        {0: {"id": None, "location": None, "version": None, "attributes": ("dict", {0: (None, None)})}},
                    ),
                    "createdOn": "datetime",
                    "lastUpdated": "datetime",
                },
                1: {
                    "siteId": None,
                    "pageId": None,
                    "type": None,
                    "scripts": ("list", {0: {"id": None, "location": None, "version": None}}),
                    "createdOn": "datetime",
                    "lastUpdated": "datetime",
                },
            },
        ),
        "pagination": {"limit": None, "offset": None, "total": None},
    }
    response = client.sites.scripts.list_custom_code_blocks(site_id="580e63e98c9a982ac9b8b741")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.sites.scripts.list_custom_code_blocks(site_id="580e63e98c9a982ac9b8b741")
    validate_response(async_response, expected_response, expected_types)

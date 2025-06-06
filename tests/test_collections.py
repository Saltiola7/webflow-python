# This file was auto-generated by Fern from our API Definition.

from webflow import Webflow
from webflow import AsyncWebflow
import typing
from .utilities import validate_response


async def test_list_(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "collections": [
            {
                "id": "63692ab61fb2852f582ba8f5",
                "displayName": "Products",
                "singularName": "Product",
                "slug": "product",
                "createdOn": "2019-06-12T13:35:14Z",
                "lastUpdated": "2022-11-17T15:08:50Z",
            },
            {
                "id": "63692ab61fb2856e6a2ba8f6",
                "displayName": "Categories",
                "singularName": "Category",
                "slug": "category",
                "createdOn": "2019-06-12T13:35:14Z",
                "lastUpdated": "2022-11-17T15:08:50Z",
            },
            {
                "id": "63692ab61fb285a8562ba8f4",
                "displayName": "SKUs",
                "singularName": "SKU",
                "slug": "sku",
                "createdOn": "2019-06-12T13:35:14Z",
                "lastUpdated": "2022-11-17T15:08:50Z",
            },
        ]
    }
    expected_types: typing.Any = {
        "collections": (
            "list",
            {
                0: {
                    "id": None,
                    "displayName": None,
                    "singularName": None,
                    "slug": None,
                    "createdOn": "datetime",
                    "lastUpdated": "datetime",
                },
                1: {
                    "id": None,
                    "displayName": None,
                    "singularName": None,
                    "slug": None,
                    "createdOn": "datetime",
                    "lastUpdated": "datetime",
                },
                2: {
                    "id": None,
                    "displayName": None,
                    "singularName": None,
                    "slug": None,
                    "createdOn": "datetime",
                    "lastUpdated": "datetime",
                },
            },
        )
    }
    response = client.collections.list(site_id="580e63e98c9a982ac9b8b741")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.list(site_id="580e63e98c9a982ac9b8b741")
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "580e63fc8c9a982ac9b8b745",
        "displayName": "Blog Posts",
        "singularName": "Blog Post",
        "slug": "post",
        "createdOn": "2016-10-24T19:41:48Z",
        "lastUpdated": "2016-10-24T19:42:38Z",
        "fields": [
            {
                "id": "23cc2d952d4e4631ffd4345d2743db4e",
                "isRequired": True,
                "isEditable": True,
                "type": "PlainText",
                "slug": "name",
                "displayName": "Name",
                "helpText": "helpText",
            }
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "displayName": None,
        "singularName": None,
        "slug": None,
        "createdOn": "datetime",
        "lastUpdated": "datetime",
        "fields": (
            "list",
            {
                0: {
                    "id": None,
                    "isRequired": None,
                    "isEditable": None,
                    "type": None,
                    "slug": None,
                    "displayName": None,
                    "helpText": None,
                }
            },
        ),
    }
    response = client.collections.create(
        site_id="580e63e98c9a982ac9b8b741", display_name="Blog Posts", singular_name="Blog Post", slug="posts"
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.create(
        site_id="580e63e98c9a982ac9b8b741", display_name="Blog Posts", singular_name="Blog Post", slug="posts"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "580e63fc8c9a982ac9b8b745",
        "displayName": "Blog Posts",
        "singularName": "Blog Post",
        "slug": "post",
        "createdOn": "2016-10-24T19:41:48Z",
        "lastUpdated": "2016-10-24T19:42:38Z",
        "fields": [
            {
                "id": "23cc2d952d4e4631ffd4345d2743db4e",
                "isRequired": True,
                "isEditable": True,
                "type": "PlainText",
                "slug": "name",
                "displayName": "Name",
                "helpText": "helpText",
            }
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "displayName": None,
        "singularName": None,
        "slug": None,
        "createdOn": "datetime",
        "lastUpdated": "datetime",
        "fields": (
            "list",
            {
                0: {
                    "id": None,
                    "isRequired": None,
                    "isEditable": None,
                    "type": None,
                    "slug": None,
                    "displayName": None,
                    "helpText": None,
                }
            },
        ),
    }
    response = client.collections.get(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.get(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.collections.delete(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.collections.delete(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )

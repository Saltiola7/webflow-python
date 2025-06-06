# This file was auto-generated by Fern from our API Definition.

from webflow import Webflow
from webflow import AsyncWebflow
import typing
from ..utilities import validate_response
from webflow import CollectionItemPostSingle
from webflow import CollectionItemPostSingleFieldData
from webflow import CollectionItemWithIdInput
from webflow import CollectionItemWithIdInputFieldData
from webflow import CollectionItem
from webflow import CollectionItemFieldData
from webflow.resources.collections.resources.items import SingleCmsItem
from webflow import CollectionItemPatchSingleFieldData


async def test_list_items(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "items": [
            {
                "id": "62b720ef280c7a7a3be8cabe",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca3",
                "lastPublished": "2022-06-30T13:35:20.878Z",
                "lastUpdated": "2022-06-25T14:51:27.809Z",
                "createdOn": "2022-06-25T14:51:27.809Z",
                "isArchived": False,
                "isDraft": False,
                "fieldData": {
                    "name": "Senior Data Analyst",
                    "slug": "senior-data-analyst",
                    "url": "https://boards.greenhouse.io/webflow/jobs/26567701",
                    "department": "Data",
                },
            },
            {
                "id": "62c880ef281c7b7b4cf9dabc",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca3",
                "lastPublished": "2023-04-15T10:25:18.123Z",
                "lastUpdated": "2023-04-10T11:45:30.567Z",
                "createdOn": "2023-04-10T11:45:30.567Z",
                "isArchived": False,
                "isDraft": False,
                "fieldData": {
                    "name": "Product Manager",
                    "slug": "product-manager",
                    "url": "https://boards.greenhouse.io/webflow/jobs/31234567",
                    "department": "Product",
                },
            },
        ],
        "pagination": {"limit": 25, "offset": 0, "total": 2},
    }
    expected_types: typing.Any = {
        "items": (
            "list",
            {
                0: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
                1: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
            },
        ),
        "pagination": {"limit": None, "offset": None, "total": None},
    }
    response = client.collections.items.list_items(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.list_items(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(async_response, expected_response, expected_types)


async def test_create_item(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.create_item(
        collection_id="580e63fc8c9a982ac9b8b745",
        request=CollectionItemPostSingle(
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemPostSingleFieldData(
                name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
            ),
        ),
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.create_item(
        collection_id="580e63fc8c9a982ac9b8b745",
        request=CollectionItemPostSingle(
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemPostSingleFieldData(
                name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
            ),
        ),
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_items(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.collections.items.delete_items(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.collections.items.delete_items(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )


async def test_update_items(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2023-03-17T18:47:35.560Z",
        "lastUpdated": "2023-03-17T18:47:35.560Z",
        "createdOn": "2023-03-17T18:47:35.560Z",
        "isArchived": True,
        "isDraft": True,
        "fieldData": {
            "name": "My new item",
            "slug": "my-new-item",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": False,
            "color": "#db4b68",
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.update_items(
        collection_id="580e63fc8c9a982ac9b8b745",
        items=[
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(name="Ne Paniquez Pas", slug="ne-paniquez-pas"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(name="No Entrar en Pánico", slug="no-entrar-en-panico"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Au Revoir et Merci pour Tous les Poissons", slug="au-revoir-et-merci"
                ),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Hasta Luego y Gracias por Todo el Pescado", slug="hasta-luego-y-gracias"
                ),
            ),
        ],
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.update_items(
        collection_id="580e63fc8c9a982ac9b8b745",
        items=[
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(name="Ne Paniquez Pas", slug="ne-paniquez-pas"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(name="No Entrar en Pánico", slug="no-entrar-en-panico"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Au Revoir et Merci pour Tous les Poissons", slug="au-revoir-et-merci"
                ),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Hasta Luego y Gracias por Todo el Pescado", slug="hasta-luego-y-gracias"
                ),
            ),
        ],
    )
    validate_response(async_response, expected_response, expected_types)


async def test_list_items_live(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "items": [
            {
                "id": "62b720ef280c7a7a3be8cabe",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca3",
                "lastPublished": "2022-06-30T13:35:20.878Z",
                "lastUpdated": "2022-06-25T14:51:27.809Z",
                "createdOn": "2022-06-25T14:51:27.809Z",
                "isArchived": False,
                "isDraft": False,
                "fieldData": {
                    "name": "Senior Data Analyst",
                    "slug": "senior-data-analyst",
                    "url": "https://boards.greenhouse.io/webflow/jobs/26567701",
                    "department": "Data",
                },
            },
            {
                "id": "62c880ef281c7b7b4cf9dabc",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca3",
                "lastPublished": "2023-04-15T10:25:18.123Z",
                "lastUpdated": "2023-04-10T11:45:30.567Z",
                "createdOn": "2023-04-10T11:45:30.567Z",
                "isArchived": False,
                "isDraft": False,
                "fieldData": {
                    "name": "Product Manager",
                    "slug": "product-manager",
                    "url": "https://boards.greenhouse.io/webflow/jobs/31234567",
                    "department": "Product",
                },
            },
        ],
        "pagination": {"limit": 25, "offset": 0, "total": 2},
    }
    expected_types: typing.Any = {
        "items": (
            "list",
            {
                0: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
                1: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
            },
        ),
        "pagination": {"limit": None, "offset": None, "total": None},
    }
    response = client.collections.items.list_items_live(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.list_items_live(collection_id="580e63fc8c9a982ac9b8b745")
    validate_response(async_response, expected_response, expected_types)


async def test_create_item_live(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.create_item_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        request=CollectionItem(
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemFieldData(
                name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
            ),
        ),
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.create_item_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        request=CollectionItem(
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemFieldData(
                name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
            ),
        ),
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_items_live(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.collections.items.delete_items_live(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.collections.items.delete_items_live(collection_id="580e63fc8c9a982ac9b8b745")  # type: ignore[func-returns-value]
        is None
    )


async def test_update_items_live(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "items": [
            {
                "id": "66f6ed9576ddacf3149d5ea6",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
                "lastPublished": "2023-03-17T18:47:35.560Z",
                "lastUpdated": "2024-09-27T17:38:29.066Z",
                "createdOn": "2024-09-27T17:38:29.066Z",
                "isArchived": True,
                "isDraft": True,
                "fieldData": {"name": "Ne Paniquez Pas", "slug": "ne-paniquez-pas", "featured": False},
            },
            {
                "id": "66f6ed9576ddacf3149d5ea6",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
                "lastPublished": "2023-03-17T18:47:35.560Z",
                "lastUpdated": "2024-09-27T17:38:29.066Z",
                "createdOn": "2024-09-27T17:38:29.066Z",
                "isArchived": True,
                "isDraft": True,
                "fieldData": {"name": "No Entrar en Pánico", "slug": "no-entrar-en-panico", "featured": False},
            },
            {
                "id": "66f6ed9576ddacf3149d5eaa",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
                "lastPublished": "2023-03-17T18:47:35.560Z",
                "lastUpdated": "2024-09-27T17:38:29.066Z",
                "createdOn": "2024-09-27T17:38:29.066Z",
                "isArchived": True,
                "isDraft": True,
                "fieldData": {
                    "name": "Au Revoir et Merci pour Tous les Poissons",
                    "slug": "au-revoir-et-merci",
                    "featured": False,
                },
            },
            {
                "id": "66f6ed9576ddacf3149d5eaa",
                "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
                "lastPublished": "2023-03-17T18:47:35.560Z",
                "lastUpdated": "2024-09-27T17:38:29.066Z",
                "createdOn": "2024-09-27T17:38:29.066Z",
                "isArchived": True,
                "isDraft": True,
                "fieldData": {
                    "name": "Hasta Luego y Gracias por Todo el Pescado",
                    "slug": "hasta-luego-y-gracias",
                    "featured": False,
                },
            },
        ]
    }
    expected_types: typing.Any = {
        "items": (
            "list",
            {
                0: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
                1: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
                2: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
                3: {
                    "id": None,
                    "cmsLocaleId": None,
                    "lastPublished": None,
                    "lastUpdated": None,
                    "createdOn": None,
                    "isArchived": None,
                    "isDraft": None,
                    "fieldData": {"name": None, "slug": None},
                },
            },
        )
    }
    response = client.collections.items.update_items_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        items=[
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(name="Ne Paniquez Pas", slug="ne-paniquez-pas"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(name="No Entrar en Pánico", slug="no-entrar-en-panico"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Au Revoir et Merci pour Tous les Poissons", slug="au-revoir-et-merci"
                ),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Hasta Luego y Gracias por Todo el Pescado", slug="hasta-luego-y-gracias"
                ),
            ),
        ],
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.update_items_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        items=[
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(name="Ne Paniquez Pas", slug="ne-paniquez-pas"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5ea6",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(name="No Entrar en Pánico", slug="no-entrar-en-panico"),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca5",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Au Revoir et Merci pour Tous les Poissons", slug="au-revoir-et-merci"
                ),
            ),
            CollectionItemWithIdInput(
                id="66f6ed9576ddacf3149d5eaa",
                cms_locale_id="66f6e966c9e1dc700a857ca4",
                field_data=CollectionItemWithIdInputFieldData(
                    name="Hasta Luego y Gracias por Todo el Pescado", slug="hasta-luego-y-gracias"
                ),
            ),
        ],
    )
    validate_response(async_response, expected_response, expected_types)


async def test_create_items(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "580e64008c9a982ac9b8b754",
        "cmsLocaleIds": ["653ad57de882f528b32e810e", "6514390aea353fc691d69827", "65143930ea353fc691d69cd8"],
        "lastPublished": "2023-03-17T18:47:35.560Z",
        "lastUpdated": "2023-03-17T18:47:35.560Z",
        "createdOn": "2023-03-17T18:47:35.560Z",
        "isArchived": True,
        "isDraft": True,
        "fieldData": {
            "name": "My new item",
            "slug": "my-new-item",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": False,
            "color": "#db4b68",
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleIds": ("list", {0: None, 1: None, 2: None}),
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.create_items(
        collection_id="580e63fc8c9a982ac9b8b745",
        cms_locale_ids=["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4", "66f6e966c9e1dc700a857ca5"],
        is_archived=False,
        is_draft=False,
        field_data=SingleCmsItem(name="Don’t Panic", slug="dont-panic"),
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.create_items(
        collection_id="580e63fc8c9a982ac9b8b745",
        cms_locale_ids=["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4", "66f6e966c9e1dc700a857ca5"],
        is_archived=False,
        is_draft=False,
        field_data=SingleCmsItem(name="Don’t Panic", slug="dont-panic"),
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get_item(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.get_item(
        collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.get_item(
        collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_item(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.collections.items.delete_item(
            collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
        )  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.collections.items.delete_item(
            collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
        )  # type: ignore[func-returns-value]
        is None
    )


async def test_update_item(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.update_item(
        collection_id="580e63fc8c9a982ac9b8b745",
        item_id="580e64008c9a982ac9b8b754",
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemPatchSingleFieldData(
            name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
        ),
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.update_item(
        collection_id="580e63fc8c9a982ac9b8b745",
        item_id="580e64008c9a982ac9b8b754",
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemPatchSingleFieldData(
            name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
        ),
    )
    validate_response(async_response, expected_response, expected_types)


async def test_get_item_live(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.get_item_live(
        collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.get_item_live(
        collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_delete_item_live(client: Webflow, async_client: AsyncWebflow) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert (
        client.collections.items.delete_item_live(
            collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
        )  # type: ignore[func-returns-value]
        is None
    )

    assert (
        await async_client.collections.items.delete_item_live(
            collection_id="580e63fc8c9a982ac9b8b745", item_id="580e64008c9a982ac9b8b754"
        )  # type: ignore[func-returns-value]
        is None
    )


async def test_update_item_live(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "id": "42b720ef280c7a7a3be8cabe",
        "cmsLocaleId": "653ad57de882f528b32e810e",
        "lastPublished": "2022-11-29T16:22:43.159Z",
        "lastUpdated": "2022-11-17T17:19:43.282Z",
        "createdOn": "2022-11-17T17:11:57.148Z",
        "isArchived": False,
        "isDraft": False,
        "fieldData": {
            "name": "Pan Galactic Gargle Blaster Recipe",
            "slug": "pan-galactic-gargle-blaster",
            "color": "#db4b68",
            "date": "2022-11-18T00:00:00.000Z",
            "featured": True,
        },
    }
    expected_types: typing.Any = {
        "id": None,
        "cmsLocaleId": None,
        "lastPublished": None,
        "lastUpdated": None,
        "createdOn": None,
        "isArchived": None,
        "isDraft": None,
        "fieldData": {"name": None, "slug": None},
    }
    response = client.collections.items.update_item_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        item_id="580e64008c9a982ac9b8b754",
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemPatchSingleFieldData(
            name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
        ),
    )
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.update_item_live(
        collection_id="580e63fc8c9a982ac9b8b745",
        item_id="580e64008c9a982ac9b8b754",
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemPatchSingleFieldData(
            name="Pan Galactic Gargle Blaster Recipe", slug="pan-galactic-gargle-blaster"
        ),
    )
    validate_response(async_response, expected_response, expected_types)


async def test_publish_item(client: Webflow, async_client: AsyncWebflow) -> None:
    expected_response: typing.Any = {
        "publishedItemIds": ["643fd856d66b6528195ee2ca", "643fd856d66b6528195ee2cb"],
        "errors": ["Staging item ID 643fd856d66b6528195ee2cf not found."],
    }
    expected_types: typing.Any = {"publishedItemIds": ("list", {0: None, 1: None}), "errors": ("list", {0: None})}
    response = client.collections.items.publish_item(collection_id="580e63fc8c9a982ac9b8b745", item_ids=["itemIds"])
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.collections.items.publish_item(
        collection_id="580e63fc8c9a982ac9b8b745", item_ids=["itemIds"]
    )
    validate_response(async_response, expected_response, expected_types)

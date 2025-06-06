# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ......core.serialization import FieldMetadata
import pydantic
import typing
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ItemsDeleteItemsLiveRequestItemsItem(UniversalBaseModel):
    item_id: typing_extensions.Annotated[str, FieldMetadata(alias="itemId")] = pydantic.Field()
    """
    Unique identifier for the Item
    """

    cms_locale_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="cmsLocaleIds")
    ] = pydantic.Field(default=None)
    """
    Array of identifiers for the locales where the item will be created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from .sku_field_data import SkuFieldData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Sku(UniversalBaseModel):
    """
    The SKU object
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the Product
    """

    cms_locale_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="cmsLocaleId")] = (
        pydantic.Field(default=None)
    )
    """
    Identifier for the locale of the CMS item
    """

    last_published: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="lastPublished")] = (
        pydantic.Field(default=None)
    )
    """
    The date the Product was last published
    """

    last_updated: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdated")] = (
        pydantic.Field(default=None)
    )
    """
    The date the Product was last updated
    """

    created_on: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdOn")] = (
        pydantic.Field(default=None)
    )
    """
    The date the Product was created
    """

    field_data: typing_extensions.Annotated[typing.Optional[SkuFieldData], FieldMetadata(alias="fieldData")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

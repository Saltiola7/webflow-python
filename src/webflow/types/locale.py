# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Locale(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the locale.
    """

    cms_locale_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="cmsLocaleId")] = (
        pydantic.Field(default=None)
    )
    """
    A CMS-specific identifier for the locale.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the locale is enabled.
    """

    display_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayName")] = (
        pydantic.Field(default=None)
    )
    """
    The display name of the locale, typically in English.
    """

    display_image_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="displayImageId")] = (
        pydantic.Field(default=None)
    )
    """
    An optional ID for an image associated with the locale, nullable.
    """

    redirect: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Determines if requests should redirect to the locale's subdirectory.
    """

    subdirectory: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subdirectory path for the locale, used in URLs.
    """

    tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A tag or code representing the locale, often following a standard format like 'en-US'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

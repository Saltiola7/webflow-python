# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .error_code import ErrorCode
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Error(UniversalBaseModel):
    code: typing.Optional[ErrorCode] = pydantic.Field(default=None)
    """
    Error code
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message
    """

    external_reference: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="externalReference")] = (
        pydantic.Field(default=None)
    )
    """
    Link to more information
    """

    details: typing.Optional[typing.List[typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Array of errors
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateStaticContentResponse(UniversalBaseModel):
    errors: typing.List[str] = pydantic.Field()
    """
    A list of error messages, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

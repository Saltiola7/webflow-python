# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import typing
from ......types.collection_item_post_single import CollectionItemPostSingle
import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class MultipleItems(UniversalBaseModel):
    items: typing.Optional[typing.List[CollectionItemPostSingle]] = pydantic.Field(default=None)
    """
    An array of items to create
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .collection_item import CollectionItem
import pydantic
from .collection_item_list_pagination import CollectionItemListPagination
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CollectionItemList(UniversalBaseModel):
    """
    Results from collection items list
    """

    items: typing.Optional[typing.List[CollectionItem]] = pydantic.Field(default=None)
    """
    List of Items within the collection
    """

    pagination: typing.Optional[CollectionItemListPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

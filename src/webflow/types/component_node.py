# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .component_property import ComponentProperty
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ComponentNode(UniversalBaseModel):
    """
    Represents a component instance within the DOM. It contains details about the component instance, such as its type and properties.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Node UUID
    """

    component_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="componentId")] = (
        pydantic.Field(default=None)
    )
    """
    Component ID
    """

    property_overrides: typing_extensions.Annotated[
        typing.Optional[typing.List[ComponentProperty]], FieldMetadata(alias="propertyOverrides")
    ] = pydantic.Field(default=None)
    """
    List of component properties with overrides for a component instance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

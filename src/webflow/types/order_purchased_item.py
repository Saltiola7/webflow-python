# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .order_price import OrderPrice
from .order_purchased_item_variant_image import OrderPurchasedItemVariantImage

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class OrderPurchasedItem(pydantic.BaseModel):
    """
    An Item that was purchased
    """

    count: typing.Optional[float] = pydantic.Field(default=None, description="Number of Item purchased.")
    row_total: typing.Optional[OrderPrice] = pydantic.Field(
        alias="rowTotal", default=None, description="The total for the row"
    )
    product_id: typing.Optional[str] = pydantic.Field(
        alias="productId", default=None, description="The unique identifier for the Product"
    )
    product_name: typing.Optional[str] = pydantic.Field(
        alias="productName", default=None, description="User-facing name of the Product"
    )
    product_slug: typing.Optional[str] = pydantic.Field(
        alias="productSlug", default=None, description="Slug for the Product"
    )
    variant_id: typing.Optional[str] = pydantic.Field(
        alias="variantId", default=None, description="Identifier for the Product Variant (SKU)"
    )
    variant_name: typing.Optional[str] = pydantic.Field(
        alias="variantName", default=None, description="User-facing name of the Product Variant (SKU)"
    )
    variant_slug: typing.Optional[str] = pydantic.Field(
        alias="variantSlug", default=None, description="Slug for the Product Variant (SKU)"
    )
    variant_image: typing.Optional[OrderPurchasedItemVariantImage] = pydantic.Field(alias="variantImage", default=None)
    variant_price: typing.Optional[OrderPrice] = pydantic.Field(
        alias="variantPrice", default=None, description="The price corresponding to the variant"
    )
    weight: typing.Optional[float] = pydantic.Field(
        default=None, description="The physical weight of the variant if provided, or null"
    )
    width: typing.Optional[float] = pydantic.Field(
        default=None, description="The physical width of the variant if provided, or null"
    )
    height: typing.Optional[float] = pydantic.Field(
        default=None, description="The physical height of the variant if provided, or null"
    )
    length: typing.Optional[float] = pydantic.Field(
        default=None, description="The physical length of the variant if provided, or null"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}

# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class StripeDetails(UniversalBaseModel):
    """
    An object with various Stripe IDs, useful for linking into the stripe dashboard.
    """

    subscription_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="subscriptionId")] = (
        pydantic.Field(default=None)
    )
    """
    Stripe-generated identifier for the Subscription
    """

    payment_method: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="paymentMethod")] = (
        pydantic.Field(default=None)
    )
    """
    Stripe-generated identifier for the PaymentMethod used
    """

    payment_intent_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="paymentIntentId")] = (
        pydantic.Field(default=None)
    )
    """
    Stripe-generated identifier for the PaymentIntent, or null
    """

    customer_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="customerId")] = pydantic.Field(
        default=None
    )
    """
    Stripe-generated customer identifier, or null
    """

    charge_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="chargeId")] = pydantic.Field(
        default=None
    )
    """
    Stripe-generated charge identifier, or null
    """

    dispute_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="disputeId")] = pydantic.Field(
        default=None
    )
    """
    Stripe-generated dispute identifier, or null
    """

    refund_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="refundId")] = pydantic.Field(
        default=None
    )
    """
    Stripe-generated refund identifier, or null
    """

    refund_reason: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="refundReason")] = (
        pydantic.Field(default=None)
    )
    """
    Stripe-generated refund reason, or null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

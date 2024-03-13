# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SkuFieldDataEcSkuBillingMethod(str, enum.Enum):
    ONE_TIME = "one-time"
    SUBSCRIPTION = "subscription"

    def visit(self, one_time: typing.Callable[[], T_Result], subscription: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkuFieldDataEcSkuBillingMethod.ONE_TIME:
            return one_time()
        if self is SkuFieldDataEcSkuBillingMethod.SUBSCRIPTION:
            return subscription()

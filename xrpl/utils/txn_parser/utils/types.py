"""Types used by the parser."""

from typing import List

from typing_extensions import TypedDict


class OptionalIssuer(TypedDict, total=False):
    """The optional issuer field for an account's balance."""

    """
    The `issuer` field is separated from `Balance` to make it
    optional, while keeping `currency` and `value` required.
    """
    issuer: str
    """The issuer of the currency. This value is optional."""


class Balance(OptionalIssuer):
    """A account's balance model."""

    currency: str
    """The currency code."""
    value: str
    """The amount of the currency."""


class AccountBalance(TypedDict):
    """A single account balance."""

    account: str
    """The affected account."""
    balance: Balance
    """The balance."""


class AccountBalances(TypedDict):
    """A model representing an account's balances."""

    account: str
    balances: List[Balance]

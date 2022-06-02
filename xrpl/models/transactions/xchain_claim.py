"""Model for a XChainClaim transaction type."""

from dataclasses import dataclass, field

from xrpl.models.required import REQUIRED
from xrpl.models.transactions.transaction import Transaction
from xrpl.models.transactions.types import TransactionType
from xrpl.models.utils import require_kwargs_on_init
from xrpl.models.xchain_claim_proof import XChainClaimProof


@require_kwargs_on_init
@dataclass(frozen=True)
class XChainClaim(Transaction):
    """Represents a XChainClaim transaction."""

    destination: str = REQUIRED  # type: ignore

    xchain_claim_proof: XChainClaimProof = REQUIRED  # type: ignore

    transaction_type: TransactionType = field(
        default=TransactionType.XCHAIN_CLAIM,
        init=False,
    )

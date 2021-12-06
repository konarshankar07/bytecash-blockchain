from dataclasses import dataclass
from typing import Optional

from bytecash.types.blockchain_format.vdf import VDFInfo, VDFProof
from bytecash.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class SignagePoint(Streamable):
    cc_vdf: Optional[VDFInfo]
    cc_proof: Optional[VDFProof]
    rc_vdf: Optional[VDFInfo]
    rc_proof: Optional[VDFProof]

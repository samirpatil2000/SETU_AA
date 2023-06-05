from enum import Enum



class ConsentStatus(Enum):
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"
    REVOKED = "REVOKED"
    PAUSED = "PAUSED"
    EXPIRED = "EXPIRED"
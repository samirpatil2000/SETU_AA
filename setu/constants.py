from enum import Enum
from typing import final
from decouple import config


SETU_API_ENDPOINT: final(str) = "https://fiu-uat.setu.co/"

X_CLIENT_ID = config('X_CLIENT_ID')
X_CLIENT_SECRET = config('X_CLIENT_SECRET')

SETU_API_HEADERS = {
  'x-client-id': X_CLIENT_ID,
  'x-client-secret': X_CLIENT_SECRET,
  'Content-Type': 'application/json'
}


class ConsentStatus(Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    REVOKED = "REVOKED"
    PAUSED = "PAUSED"
    EXPIRED = "EXPIRED"


class SessionStatus(Enum):
    COMPLETED = "COMPLETED"
    PARTIAL = "PARTIAL"
    PENDING = "PENDING"
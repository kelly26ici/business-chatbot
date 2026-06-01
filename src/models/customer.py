from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class Customer:
    phone: str
    name: Optional[str] = None
    email: Optional[str] = None
    paid: bool = False
    payment_amount: Optional[float] = None
    payment_date: Optional[str] = None
    preferences: list = field(default_factory=list)
    tags: list = field(default_factory=list)
    first_seen: str = field(default_factory=lambda: datetime.now().isoformat())
    last_seen: str = field(default_factory=lambda: datetime.now().isoformat())
    total_conversations: int = 0

    def to_dict(self) -> dict:
        return {
            "phone": self.phone,
            "name": self.name,
            "email": self.email,
            "paid": self.paid,
            "payment_amount": self.payment_amount,
            "payment_date": self.payment_date,
            "preferences": self.preferences,
            "tags": self.tags,
            "first_seen": self.first_seen,
            "last_seen": self.last_seen,
            "total_conversations": self.total_conversations
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        return cls(**data)
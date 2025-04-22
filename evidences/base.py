from abc import ABC, abstractmethod
from typing import Any


class BaseEvidence(ABC):
    @abstractmethod
    def collect(self, token: str) -> Any:
        pass
from abc import ABC, abstractmethod
from typing import Any


class AbstractBrokerInteract(ABC):
    @abstractmethod
    async def send_to_queue(self, *args: Any, **kwargs: Any):
        raise NotImplementedError

from fastapi import Depends
from faststream.kafka import KafkaBroker

from src.producer.interactors.base import AbstractBrokerInteract
from src.server.queue_app import get_kafka_broker


class KafkaBrokerInteract(AbstractBrokerInteract):
    def __init__(self, broker: KafkaBroker = Depends(get_kafka_broker)):
        self.broker = broker

    async def send_to_queue(self, data: dict, queue: str) -> None:
        return await self.broker.publish(message=data, topic=queue)




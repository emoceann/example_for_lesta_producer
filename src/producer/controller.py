import asyncio
from fastapi import Depends

from src.core.settings import Settings, get_settings
from src.producer.schemas import LogDataSchema
from src.producer.interactors.kafka_interact import KafkaBrokerInteract
from src.producer.schemas.log_schema import LogDataBQQueueSchema


class ProducerController:
    def __init__(
            self,
            kafka_interactor: KafkaBrokerInteract = Depends(),
            settings: Settings = Depends(get_settings)
    ):
        self.kafka_interactor = kafka_interactor
        self.BIG_QUERY_QUEUE = settings.BIG_QUERY_QUEUE
        self.COUCH_DB_QUEUE = settings.COUCH_DB_QUEUE

    async def publish_to_kafka_queue(self, data: LogDataSchema):
        bq_data = LogDataBQQueueSchema.model_validate(data, from_attributes=True)
        await asyncio.gather(
            self.kafka_interactor.send_to_queue(
                data.model_dump(mode="json"), self.COUCH_DB_QUEUE
            ),
            self.kafka_interactor.send_to_queue(
                bq_data.model_dump(mode="json"), self.BIG_QUERY_QUEUE
            )
        )

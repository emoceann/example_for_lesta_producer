from functools import lru_cache

from faststream.kafka import KafkaBroker

from src.core.settings import get_settings

settings = get_settings()

kafka_broker = KafkaBroker(bootstrap_servers=settings.KAFKA_URL)


@lru_cache
def get_kafka_broker() -> KafkaBroker:
    return kafka_broker

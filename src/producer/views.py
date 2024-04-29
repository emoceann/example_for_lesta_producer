from fastapi import APIRouter, Depends, status

from src.producer.controller import ProducerController
from src.producer.schemas.log_schema import LogDataSchema

router = APIRouter()


@router.post(
    "/log",
    status_code=status.HTTP_200_OK
)
async def send_log_to_consumer(
        data: LogDataSchema,
        controller: ProducerController = Depends()
):
    return await controller.publish_to_kafka_queue(data)

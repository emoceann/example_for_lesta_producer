from typing_extensions import TypedDict

from pydantic import BaseModel, AnyUrl, IPvAnyNetwork, Json, TypeAdapter, field_validator

json_adapter = TypeAdapter(Json)


class BaseContextSchema(BaseModel):
    extra: str | None = None
    project: str | None = None
    contacts: dict | None = None


class ContextSchema(BaseContextSchema):
    extra: dict | None = None
    utm_json: dict | None = None
    webhook_log: dict | None = None
    request_type: str | None = None


class ContextSchemaBQ(BaseContextSchema):
    @field_validator("extra", mode="before")
    def to_json(cls, value: dict):
        return json_adapter.dump_json(value)


class BaseOperationsSchema(BaseModel):
    action: str | None = None
    listing_ref: str | None = None
    url: AnyUrl | None = None
    origin: AnyUrl | str = None
    message_type: str | None = None


class OperationsSchema(BaseOperationsSchema):
    listing_id: int | None = None


class MetaSchema(TypedDict):
    user_agent: str
    language: str


class LogDataSchemaBase(BaseModel):
    name: str
    session_id: str
    lead_id: int | None = None
    timestamp: float
    partition: str


class LogDataSchema(LogDataSchemaBase):
    operations: OperationsSchema
    ip: IPvAnyNetwork
    context: ContextSchema
    meta: MetaSchema


class LogDataBQQueueSchema(LogDataSchemaBase):
    operations: BaseOperationsSchema
    ip: IPvAnyNetwork
    context: ContextSchemaBQ
    meta: MetaSchema

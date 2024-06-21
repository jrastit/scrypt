from datetime import datetime
from dataclasses_jsonschema import JsonSchemaMixin
from sqlalchemy.orm import Mapped

from scrypt.model.db import (
    Base,
    intpk,
    column_id,
    column_string_null,
    column_time_created,
    column_time_updated,
)


class Variable(Base, JsonSchemaMixin):
    __tablename__ = "variable"
    id: Mapped[intpk] = column_id()
    time_create: Mapped[datetime] = column_time_created()
    time_updated: Mapped[datetime] = column_time_updated()

    name: Mapped[str] = column_string_null()
    description: Mapped[str] = column_string_null()

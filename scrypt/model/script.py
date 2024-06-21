from datetime import datetime
from dataclasses_jsonschema import JsonSchemaMixin
from sqlalchemy.orm import Mapped

from scrypt.model.db import (
    db,
    Base,
    column_foreign_key,
    column_position,
    intpk,
    column_id,
    column_string_null,
    column_time_created,
    column_time_updated,
)


class Script(Base, JsonSchemaMixin):
    __tablename__ = "script"
    id: Mapped[intpk] = column_id()
    time_create: Mapped[datetime] = column_time_created()
    time_updated: Mapped[datetime] = column_time_updated()

    name: Mapped[str] = column_string_null()
    description: Mapped[str] = column_string_null()
    content: Mapped[str] = column_string_null()
    prompt: Mapped[str] = column_string_null()

    position: Mapped[float] = column_position()

    flavor_id: Mapped[int] = column_foreign_key("flavor.id")

    parent_id: Mapped[int] = db.Column(
        db.Integer, db.ForeignKey("script.id"), nullable=True, default=None
    )

    # parent: Mapped["Script"] = db.relationship(
    #     "Script",
    #     remote_side=[id],
    #     # back_populates="childrens",
    # )

    # childrens = column_relationship_ordering_list(
    #     "Script",
    #     back_populates="parent",
    #     order_by="position",
    # )

from dataclasses_jsonschema import JsonSchemaMixin
from sqlalchemy.orm import Mapped

from scrypt.model.db import (
    Base,
    column_foreign_key,
    intpk,
    column_id,
)


class ScriptVariableInput(Base, JsonSchemaMixin):
    __tablename__ = "script_variable"
    id: Mapped[intpk] = column_id()

    script_id: Mapped[int] = column_foreign_key("script.id")
    variable_id: Mapped[int] = column_foreign_key("variable.id")

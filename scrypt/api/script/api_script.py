#!/usr/bin/3
from flask import request, Blueprint

from scrypt.api.api_key import require_appkey
from scrypt.model.script import Script
from scrypt.utils.db_util import (
    inset_or_update_object_from_json,
    delete_object,
    get_object,
)

script_api = Blueprint("script_api", __name__)


@script_api.route("/api/script", methods=["PUT"])
@require_appkey
def api_script_put():
    """Create or update a Script object
    ---
    put:
        description: Put a new Script or update it
        response:
            200:
                content:
                    application/json:
                        schema: Script

    """
    return inset_or_update_object_from_json(Script, request.json)


@script_api.route("/api/script/<script_id>", methods=["GET"])
@require_appkey
def api_script_get(script_id):
    return get_object(Script, script_id)


@script_api.route("/api/script/<script_id>", methods=["DELETE"])
@require_appkey
def api_script_delete(script_id):
    return delete_object(Script, script_id)

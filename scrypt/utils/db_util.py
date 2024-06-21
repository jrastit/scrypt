from scrypt.model.db import db
from flask import jsonify


def inset_or_update_object_from_json_raw(mapper, data):
    if "id" not in data or not data["id"]:
        # user = User(**{k: v for k, v in obj.items() if k in {'id', 'name'}})
        db.session.bulk_insert_mappings(mapper, [data])
    else:
        db.session.bulk_update_mappings(mapper, [data])
    db.session.commit()
    ret = db.session.query(mapper).filter_by(name=data["name"]).first()
    return ret


def inset_or_update_object_from_json(mapper, data):
    return jsonify(
        {mapper.__name__: inset_or_update_object_from_json_raw(mapper, data)}
    )


def get_object_list(mapper):
    return jsonify({mapper.__name__: db.session.query(mapper).all()})


def get_object(mapper, id):
    return jsonify(
        {mapper.__name__: db.session.query(mapper).filter_by(id=id).first()}
    )


def delete_object(mapper, id):
    db.session.query(mapper).filter_by(id=id).delete()
    db.session.commit()
    return {"Status": "success"}

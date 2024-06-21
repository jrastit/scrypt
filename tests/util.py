from scrypt.model.flavor import Flavor
from scrypt.model.db import db
from scrypt.model.flavor import Flavor
from scrypt.model.db import db


def get_python_flavor():
    flavor = db.session.query(Flavor).filter_by(name="python").first()
    if not flavor:
        with open("resource/python_prompt.txt", "r") as file:
            prompt = file.read()
        flavor = Flavor(name="python", description="python", prompt=prompt)
        db.session.add(flavor)
        db.session.commit()
    return flavor

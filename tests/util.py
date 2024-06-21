from scrypt.model.flavor import Flavor
from scrypt.model.db import db
from scrypt.model.flavor import Flavor
from scrypt.model.db import db
import os


def get_python_flavor():
    flavor = db.session.query(Flavor).filter_by(name="python").first()
    if not flavor:
        current_directory = os.getcwd()
        print(current_directory)
        with open(
            os.path.join(current_directory, "resource/python_prompt.txt"), "r"
        ) as file:
            prompt = file.read()
        flavor = Flavor(name="python", description="python", prompt=prompt)
        db.session.add(flavor)
        db.session.commit()
    return flavor

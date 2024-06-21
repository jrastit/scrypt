from scrypt.model.flavor import Flavor
from scrypt.model.script import Script

from scrypt.model.db import db


def test_data_flavor(app):
    flavor = Flavor(
        name="python",
        description="python",
    )
    db.session.add(flavor)
    db.session.commit()


def test_data_script(app):
    flavor = db.session.query(Flavor).filter_by(name="python").first()
    if not flavor:
        flavor = Flavor(
            name="python",
            description="python",
        )
        db.session.add(flavor)
        db.session.commit()

    script = Script(
        name="test_script",
        content='print("hello world")',
        description="test script",
        flavor_id=flavor.id,
        parent_id=None,
    )
    db.session.add(script)
    db.session.commit()

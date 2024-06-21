from scrypt.model.flavor import Flavor
from scrypt.model.script import Script

from scrypt.model.db import db
from tests.util import get_python_flavor


def test_data_flavor(app):
    flavor = Flavor(
        name="python",
        description="python",
    )
    db.session.add(flavor)
    db.session.commit()


def test_data_script(app):
    flavor = get_python_flavor()

    script = Script(
        name="test_script",
        content='print("hello world")',
        description="test script",
        flavor_id=flavor.id,
        parent_id=None,
    )
    db.session.add(script)
    db.session.commit()

import pytest

from scrypt.myapp import init_app
from scrypt.utils.thread import get_nb_thread, set_thread_available


@pytest.fixture
def app():
    app = init_app()
    return app


@pytest.fixture()
def thread_check():

    set_thread_available(1)

    """Fixture to execute asserts before and after a test is run"""
    # Setup: fill with any logic you want
    assert get_nb_thread() == 0

    yield  # this is where the testing happens

    assert get_nb_thread() == 0

    set_thread_available(0)

    # Teardown : fill with any logic you want

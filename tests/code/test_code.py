from scrypt.code.gen_code import gen_code
from scrypt.code.python_exec import python_exec
from tests.util import get_python_flavor


def test_code_hello_wold(app):
    flavor = get_python_flavor()
    script = gen_code(
        flavor,
        "test_script",
        "create code that return as variable 'gretting' with value 'hello world'",
    )
    print(script.content)
    ret = python_exec(script)
    assert ret["greeting"] == "hello world"


def test_code_fibonacci(app):
    flavor = get_python_flavor()
    script = gen_code(
        flavor,
        "test_script_fibonacci",
        """
        create code that calculate the fibonacci sequence
        
        the input is variable 'n'
        set the result as variable 'ret'"
        """,
    )
    print(script.content)
    ret = python_exec(script, {"n": 9})
    assert ret["ret"] == 34

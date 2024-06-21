from scrypt.code.gen_code import code_exec, code_gen, code_static
from tests.util import get_python_flavor


def test_code_hello_wold(app):
    flavor = get_python_flavor()
    script = code_gen(
        flavor,
        "test_script",
        "create code that return as variable 'gretting' with value 'hello world'",
    )
    print(script.content)
    ret = code_exec(script)
    assert ret["greeting"] == "hello world"


def test_code_fibonacci(app):
    flavor = get_python_flavor()
    script = code_gen(
        flavor,
        "test_script_fibonacci",
        """
        create a function call fibonacci that calculate the fibonacci sequence and return the value at the asked rank
        parameter is n the rank of the fibonacci sequence
        
        """,
    )
    script_call = code_static(
        flavor,
        "test_script_fibonacci_call",
        """
assert fibonacci(9) == 21
assert fibonacci(10) == 34       
ret = fibonacci(n)
       
        """,
    )
    # print(script.content)
    ret = code_exec([script, script_call], {"n": 9})
    assert ret["ret"] == 21
    ret = code_exec([script, script_call], {"n": 10})
    assert ret["ret"] == 34


def test_code_system(app):
    flavor = get_python_flavor()
    script = code_gen(
        flavor,
        "test_script_system",
        """
        create a function call 'system_exec' that execute 'ls' in the current dir 
        and parse the stdout and return a list of string
        and return the list of string
        
        parse the stdout and return a liste of string
        """,
    )
    script_call = code_static(
        flavor,
        "test_script_system_call",
        """
ret = system_exec()
        """,
    )
    ret = code_exec([script, script_call])
    assert "scrypt" in ret["ret"]
    print(ret)

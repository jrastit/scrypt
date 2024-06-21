from typing import List
from scrypt.model.script import Script


def python_exec(script: List[Script], local_vars: dict = {}):
    content = script[0].content
    for script in script[1:]:
        content = content + "\n" + script.content
    print(content)
    code_block = compile(content, "code.py", "exec")
    exec(code_block, globals(), local_vars)
    return local_vars

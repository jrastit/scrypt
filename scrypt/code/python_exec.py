from scrypt.model.script import Script


def python_exec(script: Script, local_vars: dict = {}):
    exec(script.content, None, local_vars)
    return local_vars

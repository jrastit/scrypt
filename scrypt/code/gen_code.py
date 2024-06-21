from typing import List
from scrypt.code.python_exec import python_exec
from scrypt.model.flavor import Flavor
from scrypt.model.script import Script
from scrypt.model.db import db
from scrypt.service.openai_service import call_openai_sdk


def code_gen(
    flavor: Flavor,
    name: str,
    prompt: str,
    parent_id: int = None,
    description: str = None,
):
    system_prompt = flavor.prompt
    content = call_openai_sdk(
        prompt,
        system_prompt,
        # model="gpt-3.5-turbo-0125",
        model="gpt-4o",
    )
    if "```python" in content:
        start_index = content.find("```python")
        end_index = content.find("```", start_index + len("```python"))
        if start_index == -1 or end_index == -1:
            raise ValueError(
                "Generated content does not contain valid Python code."
            )
        content = content[start_index + len("```python") : end_index]

    script = Script(
        name=name,
        content=content,
        prompt=prompt,
        description=description,
        flavor_id=flavor.id,
        parent_id=parent_id,
    )
    db.session.add(script)
    db.session.commit()
    return script


def code_static(
    flavor: Flavor,
    name: str,
    content: str,
    parent_id: int = None,
    description: str = None,
):
    script = Script(
        name=name,
        content=content,
        description=description,
        flavor_id=flavor.id,
        parent_id=parent_id,
    )
    db.session.add(script)
    db.session.commit()
    return script


def code_exec(script: List[Script], local_vars: dict = {}):
    if not script or not script[0]:
        raise ValueError("Script is not valid")
    for i in range(1, len(script)):
        if script[i].flavor_id != script[0].flavor_id:
            raise ValueError("Script is not valid, wrong flavor")
    flavor_id = script[0].flavor_id
    flavor = db.session.query(Flavor).get(flavor_id)
    if flavor.name == "python":
        return python_exec(script, local_vars)

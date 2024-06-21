from scrypt.model.flavor import Flavor
from scrypt.model.script import Script
from scrypt.model.db import db
from scrypt.service.openai_service import call_openai_sdk


def gen_code(
    flavor: Flavor,
    name: str,
    prompt: str,
    parent_id: int = None,
    description: str = None,
):
    system_prompt = flavor.prompt
    content = call_openai_sdk(
        prompt, system_prompt, model="gpt-3.5-turbo-0125"
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
        description=description,
        flavor_id=flavor.id,
        parent_id=parent_id,
    )
    db.session.add(script)
    db.session.commit()
    return script

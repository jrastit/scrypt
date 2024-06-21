import openai
from scrypt.config import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)


def call_openai_sdk(prompt, system_prompt, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content

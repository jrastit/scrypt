from scrypt.service.openai_service import call_openai_sdk


def test_call_openai_sdk():
    prompt = "dis bonjour"
    system_prompt = "Answer the question in french"  # Add your system prompt here if needed

    # Call the call_openai_sdk function with the given prompt
    response = call_openai_sdk(
        prompt, system_prompt, model="gpt-3.5-turbo-0125"
    )

    # Add your assertions or checks here to validate the response

    # Example assertion:
    assert "bonjour" in response.lower()

    # Add more assertions or checks as needed

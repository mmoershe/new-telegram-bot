from ollama import chat, ChatResponse


def generate_response(message: str) -> str: 
    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': message.strip(),
    },
    ])
    return str(response.message.content)

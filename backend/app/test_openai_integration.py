import asyncio
from typing import List

# Define the Message class directly in this file
class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

# Define the function to be tested
async def get_llm_response(messages: List[Message]) -> str:
    import httpx
    import os
    
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": message.role, "content": message.content} for message in messages]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()
    
    return result['choices'][0]['message']['content']

# Test the function
async def main():
    # Prepare test messages
    test_messages = [
        Message(role="system", content="You are a helpful assistant."),
        Message(role="user", content="Tell me a joke.")
    ]
    
    try:
        response = await get_llm_response(test_messages)
        print("Response from OpenAI:", response)
    except Exception as e:
        print("Error:", str(e))

# Run the test script
if __name__ == "__main__":
    asyncio.run(main())

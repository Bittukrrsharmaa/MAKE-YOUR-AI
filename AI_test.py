import os
from openai import OpenAI
from dotenv import load_dotenv
from tools import TOOLS

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

stream = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role" :"user","content": "tell me the weather of pune and wather of delhi"}],
    tools= TOOLS,
    stream=True,
)
full_response =""

for chunk in stream:
    if not chunk.choices:
        continue

    piece =chunk.choices[0].delta
    if piece:
        print(piece,end="",flush= True)
        full_response += piece

print("\n Full response:")
print(full_response)


from openai import OpenAI

# pip install openai

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<Your API Key Here>",
)

completion = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "system",
            "content": "You are a person named Daksh who speaks Hindi as well as English. You are from India and you are a Bachelor Of Science Student in Applied Artificial Intelligence and Data Science at IIT Jodhpur. You analyze chat history and respond like Daksh. The respond should be very short.The output should always short and in English or Hinglish"
        },
        {
            "role": "user",
            "content": "Hello, introduce yourself."
        }
    ]
)

print(completion.choices[0].message.content)
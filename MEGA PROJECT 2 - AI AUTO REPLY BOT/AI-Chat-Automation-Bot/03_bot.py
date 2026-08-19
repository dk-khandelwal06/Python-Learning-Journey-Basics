import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<Your API Key Here>",
)

def is_last_message_from_sender(chat_log, sender_name="Daksh Khandelwal"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return False 
    return True
    

# Step 1: Click on the Chrome icon 
pyautogui.click(1023, 1054)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(5)
    # Step 2: Select the WhatsApp chat text
    pyautogui.moveTo(2606,235)
    pyautogui.dragTo(3489, 941, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(3111, 584)

    # Step 4: Get chat history from clipboard
    chat_history = pyperclip.paste()
    if not chat_history.strip():
        print("Nothing was copied. Trying again...")
        continue

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": """
You are Daksh, Bachelor Of Science Student in Applied Artificial Intelligence and Data Science at IIT Jodhpur.

Analyze the WhatsApp chat history and generate the next natural reply as Daksh.

The reply should:
- Sound natural and conversational.
- Match the language and tone of the conversation.
- Be concise like a normal WhatsApp message.
- Use Hindi, English, or Hinglish depending on the conversation.
- Do not explain your reasoning.
- Output only the message that should be sent.
"""
                },
                {
                    "role": "system",
                    "content": "Do not include timestamps, sender names, or prefixes in your response."
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
        )

        response = completion.choices[0].message.content
        print("AI Response:", response)
        pyperclip.copy(response)

        # Step 5: Click at coordinates
        pyautogui.click(3111, 994)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')
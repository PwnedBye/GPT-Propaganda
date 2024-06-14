import openai

openai.api_key = 'your-api-key'

def ask_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

user_input = input("Ask something: ")

response = ask_chatgpt(user_input)

print("Response:", response)

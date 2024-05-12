from openai import OpenAI
from env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


user_message = ''

messages=[
    {"role": "system", "content": "You are a counselor. You must remember user's name. You must use Korean."},
]

while user_message != 'exit':
    user_message = input('사용자\t: ')
    messages.append({"role": "user", "content": user_message})
    
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0.3,
        messages=messages
    )
    
    
    messages.append({"role": "assistant", "content": completion.choices[0].message.content})
    
    print("GPT\t: ", completion.choices[0].message.content)
    
    # print('-------------------')
    # for m in messages:
    #     print(f"\t\t{m['role']}\t: {m['content']}")
    # print('================')
    
    
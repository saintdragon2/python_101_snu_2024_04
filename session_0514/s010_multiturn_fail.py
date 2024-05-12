from openai import OpenAI
from env import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


user_message = ''

while user_message != 'exit':
    user_message = input('사용자:\t')
    
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "너는 상담사 역할을 맡았다. 사용자의 이름을 물어보고, 사용자의 고민을 듣고 답변해줘."},
            {"role": "user", "content": user_message},
        ]
    )
    
    print("GPT:\t", completion.choices[0].message.content)
    
###
# 사용자: 안녕하세요 
# GPT  :  안녕하세요! 반갑습니다. 이름이 어떻게 되세요?
# 사용자 : 제 이름은 홍길동 입니다.  서울대학교에서 교수를 하고 있어요. 
# GPT  :     안녕하세요, 홍길동 교수님! 서울대학교에서 교수로 계시다니 정말 대단하시네요. 교수님의 고민이나 저에게 도움을 요청하실 사항이 있으신가요?
# 사용자 : 제 이름이 뭘까요? 
# GPT  :     제가 사용자님의 개인 정보를 저장하거나 알지 못하기 때문에 사용자님의 이름을 정확히 알 수 없습니다. 사용자님이 이름을 알려주시면 그 이름으로 대화를 이어갈 수 있습니다. 이름을 알려주시겠어요?
# 사용자 : 홍길동라고요. 
# GPT  :     안녕하세요, 홍길동님! 만나서 반갑습니다. 무엇에 대해 이야기하고 싶으신가요? 어떤 고민이 있으시다면 편하게 말씀해주세요.
# 사용자 : 제 이름은 뭘까요? 
# GPT :     저는 이름을 정하지 않았습니다. 혹시 어떤 이름으로 부르면 좋을지 알려주시겠어요?

####

#### 이름을 기억을 못한다. 
from openai import OpenAI
from zipfile import ZipFile
key = open('key', 'r').readline().rstrip()
client = OpenAI(api_key=key)

prompt = \
'''
Analyze this log of a WhatsApp chat of friends and based on it construct three statements for a fun quiz for the friends about their memories
two of which are false and only one is true
print the statement followed by a comma and space, then print True or False
use stricktly the provided response template 

response template:
    [Statement1] -> [False]
    [Statement2] -> [True]
    [Statement3] -> [False]
    

'''

def gpt(data):
    query = prompt + data
    messages=[
        {"role": "user", 
            "content": query
        }]
    chat = client.chat.completions.create(model='gpt-4-turbo', messages=messages)
    reply = chat.choices[0].message.content
    return reply
    

def extractData(path):
    with ZipFile(path, 'r') as zObject: 
       zObject.extractall(path="chat/") 
    chat=''
    with open('chat/_chat.txt') as f:
        lines = f.readlines()
    chat=''.join(lines[-min(1500, len(lines)):])
    return gpt(chat)
datum=[]
for _ in range(5):
    question=extractData('chat.zip')
    parts=question.split('\n')
    data=[]
    for part in parts:
        temp=part.split('->')
        if 'True' in temp[1]:
            temp[1]='True'
        if 'False' in temp[1]:
            temp[1]='False'
        data.append(temp)
    datum.append(data)
print(datum)





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
    [Statement1], [False]
    [Statement2], [True]
    [Statement3], [False]
    

'''

def gpt(data):
    #prompt='Analyze this log of a WhatsApp chat of friends and based on it construct three statements for a fun quiz for the friends about their memories, two of which are false and only one is true'
    query = prompt + data
    messages=[
        {"role": "user", 
            "content": query
        }]
    chat = client.chat.completions.create(model='gpt-4-turbo', messages=messages)
    reply = chat.choices[0].message.content

    
    print(f'ChatGPT: {reply}')

def extractData(path):
    with ZipFile(path, 'r') as zObject: 
       zObject.extractall(path="chat/") 
    #file= open('chat/_chat.txt')
    chat=''
    with open('chat/_chat.txt') as f:
        lines = f.readlines()
    chat=''.join(lines[-min(1500, len(lines)):])
    return gpt(chat)

extractData('chat.zip')
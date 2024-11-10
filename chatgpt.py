from openai import OpenAI
from zipfile import ZipFile
key = open('key', 'r').readline().rstrip()
client = OpenAI(api_key=key)
prompt = \
'''
Read this chat log and identify top 5 most memorable events. You should:
 
record the time of the choosen event.
make a title of the event.
add the photo name if any relevant
use stricktly the provided response template

Here are examples of your 
 
task:[dd/mm/yy, hh/mm/ss] User1: There is this event happening tonight at X.<attached flag FILENAME>[dd/mm/yy, hh/mm/ss] User2: Sounds cool, I'll join you.

    .....

    [dd/mm/yy, hh/mm/ss] User1: Wanna go to Y. 
    [dd/mm/yy, hh/mm/ss] User2: Sure.

    .....

    [dd/mm/yy, hh/mm/ss] User1: Didn't manage to do my homework tonight. 
    [dd/mm/yy, hh/mm/ss] User2: Sad....

 
response:

    [dd/mm/yy, hh/mm/ss] "attending event at X" FILENAME
    [dd/mm/yy, hh/mm/ss] "going to Y" 

data log:

'''


def gpt(data):
    query = prompt + data
    messages=[
        {'role': 'user', 'content': query}
    ]
    chat = client.chat.completions.create(model='gpt-4-turbo', messages=messages)
    reply = chat.choices[0].message.content
    return reply


def extractData_timeline(path):
    with ZipFile(path + "/chat.zip", 'r') as zObject: 
       zObject.extractall(path) 
    #file= open('chat/_chat.txt')
    chat=''
    with open(path + '/_chat.txt') as f:
        lines = f.readlines()
    chat=''.join(lines[-min(1500, len(lines)):])
    output=gpt(chat)
    return output

def extractData_quiz(path):
    with ZipFile(path, 'r') as zObject: 
       zObject.extractall(path="chat/") 
    #file= open('chat/_chat.txt')
    chat=''
    with open(path + '/_chat.txt', 'r') as f:
        lines = f.readlines()
    chat=''.join(lines[-min(1500, len(lines)):])
    return gpt(chat)

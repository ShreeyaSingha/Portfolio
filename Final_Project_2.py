from random import choice
import json

def greetUser(name):
    if name == "":
        print("I suppose your name shall remain a mystery.")
        return "[]"
    else:
        print(f"Hello, {name}. Good to meet you!")
        return name

def getAgentName():
    names = ['Lester', 'Randolph', 'Issac', 'Hiram', 'Marcos', 'Kory', 'Desmond', 'Kent', 'Angel', 'Jeremiah', 'Camille', 'Casey', 'Velma', 'Rebekah', 'Lilian', 'Claudia', 'Cassie', 'Tammi', 'Dionne', 'Kirsten', 'Leonardo', 'Don', 'Thaddeus', 'Parker', 'Hank', 'Emerson', 'Scott', 'Albert', 'Robby', 'Eldon', 'Vanessa', 'Claudia', 'Shelby', 'Minerva', 'Chasity', 'Mercedes', 'Beulah', 'Patrica', 'Lavonne', 'Leona']
    return choice(names)

def logChat(name, message):
    log = open("chat_log.txt", 'a')
    log.write(f"{name}: {message} \n")
    log.close()

def respond(prompt, agent, name):
    global responses
    global exitPrompts
    logChat(name, prompt)
    for i in responses.keys():
        if prompt.lower() in exitPrompts:
            return
        elif i in prompt:
            response = responses[i]
            logChat(agent, response)
            break
        else:
            response = choice(["Please explain further.", "Can you tell me more?", "I see, could you expand?"])
            logChat(agent, response)
    print(f"{agent}:", response)
    nextPrompt = input("You: ")
    logChat(name, nextPrompt)
    if nextPrompt.lower() in exitPrompts:
        return
    else:
        respond(nextPrompt, agent, name)

#main
userName = input("Hello! Who am I speaking with? ")
userName = greetUser(userName)
print("Please wait and agent will be with you shortly...")
agentName = getAgentName()
print(f"My name is {agentName}. What can I help you with?")
prompt = input("You: ")
global responses
global exitPrompts
exitPrompts = ['bye', 'quit', 'exit', 'done', 'thank you', 'thanks', 'ok bye', 'ok thank you', 'ok thanks', 'ok, bye', 'ok, thank you', 'ok, thanks']
if prompt.lower() in exitPrompts:
    SystemExit
f = open("responses.json", "r")
responses = {}
responses = json.load(f)
respond(prompt.lower(), agentName, userName)
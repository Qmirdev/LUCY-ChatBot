import datetime
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["Hi", ["Hello", "Hey there!"]],
]

chat = Chat(pairs, reflections)

def log_conversation(user_input, bot_response):
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open('chat-log.txt', 'a') as f:
    f.write("{} User: {}\n".format(timestamp, user_input))
    f.write("{} Bot: {}\n".format(timestamp, bot_response))

print("Hello, I'm Chatbot! Ask me something.")
while True:
  user_input = input("You: ")
  bot_response = chat.respond(user_input)

  print("Bot: {}".format(bot_response))

  log_conversation(user_input, bot_response)
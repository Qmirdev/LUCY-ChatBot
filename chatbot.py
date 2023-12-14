import datetime
import nltk
from nltk.chat.util import Chat, reflections
import pairs

# pairs.py

chat = Chat(pairs.pairs, reflections)

def log_conversation(user_input, bot_response):
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  with open('chat-log.txt', 'a') as f:
    f.write("{} User: {}\n".format(timestamp, user_input))
    f.write("{} Lucy: {}\n".format(timestamp, bot_response))

print("Hello, I'm Lucy!")
while True:
  user_input = input("You: ")
  bot_response = chat.respond(user_input)

  print("Lucy: {}".format(bot_response))

  log_conversation(user_input, bot_response)
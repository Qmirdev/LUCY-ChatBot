import datetime
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["Hi", ["Hello", "Hey there!"]],
]

chat = Chat(pairs, reflections)

chat.converse()
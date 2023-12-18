# L U C Y
<img src="https://github.com/Qmirdev/LUCY-ChatBot/blob/main/doc/1.png">
This is a simple chatbot program written in Python. It uses the NLTK library for natural language processing and has a basic conversational engine based on predefined response pairs.

## Features
- Responds to user input using a matching response from a predefined list
- Logs all conversations to a text file with timestamps
- Built using NLTK for basic NLP capabilities like stemming and lemmatization

## Usage
the dependencies needed to run the chatbot.py Python project are:

1. **datetime**: This module comes with Python standard library, so no separate installation needed. It is used for timestamping the chat logs.
2. **nltk**: The Natural Language Toolkit library needs to be installed. This can be installed via `pip install nltk`. NLTK provides the chatbot engine and NLP capabilities.

> [!NOTE]
> Simply Install all needed dependencies with executing `pip install -r requirements.txt` in the project directory.


To use the chatbot, simply run the `chatbot.py` script:

```
python3 chatbot.py
```

The bot will introduce itself and then you can start chatting by typing messages and pressing enter. The bot will respond based on the rules in `pairs.py`.

All conversations are logged to `chat-log.txt` with timestamps.

## Customizing
The bot's conversational capabilities are based on the `pairs.py` file which contains the predefined input/response pairs. To customize the bot's behavior, you can modify this file.

You can also customize the bot's name, greeting messages, etc by modifying the `chatbot.py` source code.

## Future Plans
This is just a simple prototype chatbot, but it can be extended and improved in many ways:

- Add a graphical user interface
- Integrate with external APIs for things like weather, news, etc
- Implement more advanced NLP using deep learning for better language understanding
- Allow the bot to learn from conversations and expand its knowledge base
- Deploy the bot to a production environment like Telegram, Slack, etc

## License
This project is licensed under the MIT license. Feel free to use and modify the code as you like.

## Contributing
Contributions to improve the bot's capabilities are welcome! Please open issues and pull requests on GitHub.

So in summary, this is a simple open source Python chatbot that can be customized and extended. Check out the code, try out the live bot, and feel free to contribute!

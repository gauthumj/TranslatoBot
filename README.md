# TranslatoBot
Translator bot for telegram that can translate messages from any language to english !

# Working
The main modules are requests for accessing the telegram API for bots, googletrans for translating from any language to english and json to read the data returned from the API. 
The translato class takes care of reading the token from the config.cfg file, getting updates from the bot API and writing the reply back to user using the chat id through the API.

NOTE: the googletrans module is unstable and its advisable to install it using : pip install git+https://github.com/BoseCorp/py-googletrans.git --upgrade

it also times out the server after inactivity or returns None requiring the server to be restarted. This has been fixed by using subprocess.Popen to run the server.py file. when an error occurs due to googletrans, the server will be automatically restarted.

# Translato in action 

![alt text](https://github.com/gauthumj/TranslatoBot/blob/main/Translato.jpg?raw=true)

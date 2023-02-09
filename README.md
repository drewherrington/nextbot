# Nextbot

## Introduction

This project is a chatbot built using the rule-based approach where the bot makes replies based on a set of pre-determined responses. The bot uses TensorFlow and Keras for its model training the Chatbot using a custom-compiled dataset. The model is retrieval based, meaning that the Chatbot uses a heuristic to select a response from the library's predefined responses. The Chatbot uses the received message from the user during the conversation to select the best response within that context. For example, when greeting the bot, it will analyse the message from the user and select a random greeting response from the dataset previously trained. This project also uses the Python library NLTK to pre-process the received user messages.

Rule-based chatbots are relatively simple to use. A database of replies is available through the packages, together with a set of guidelines that make it easier for them to find the right one in the database. Of course, they cannot produce their solutions, but with an extensive database of solutions and cleverly established rules, they may be valuable and productive.

This Chatbot uses the most basic Rule-based One-to-one tables of inputs and answers. Therefore, these bots are tightly constrained and can only react to requests if the inputs they are given match exactly. Note that this Chatbot project used an Apple MacBook Air with an Intel chip, which is vital information since the bot used TensorFlow packages and different versions of TensorFlow for Apple MacBooks exist.

As mentioned previously, the project uses The Natural Language Toolkit library. Using the NLTK library (NLTK) makes it simple to handle human language data. In addition, it gives access to several text-processing libraries and simple user interfaces for various language-based resources, including the Open Multilingual Wordnet.

This project also includes the usage of regular expressions. A regular expression is a unique set of characters that, when combined with a particular syntax, makes it easier to look for and identify word, phrase, and letter patterns in collections of strings. In UNIX, they are frequently used for text searching and matching. The "re" module in Python provides regular expression functionality.

A rule-based chatbot will operate by looking for particular keywords in user-provided inputs.
The keywords determine the user's purpose or the desired course of action. Then, the bot automatically generates a suitable answer from the package library according to the chatbot's use case. Finally, a manual list of keywords and a dictionary of possible answers create a response.

To search the user input for terms kept in the value field of the keywords dict dictionary, we employ the RegEx Search function. The values in the keywords bag of words pickle file included with this project dictionary have unique meta-character formatting. These sequences are used by the RegEx search function to compare character patterns in the input string with character patterns in the keywords. In the event that a match is discovered, the current intent is chosen and utilised as the key to the answers dictionary to choose the appropriate response.

### Training Data

The dataset used for this model was compiled manually since it only comprises of simple responses to atypical conversation between a user and an assumed support agent. Each request patter and responses are categorised into intents so the model is able to identify the context of the conversation.

## Set up

The chatbot is exposed to external services through a Python HTTP web framework. In this case Flask was used to create a simple wrapper to send and receive messages. To demonstrate the practical use of the chatbot a demo website has also been included with data included as built in JSON structures.

### Chatbot

The chatbot is built using Python and relative packages. The bot was developed within a Python virtual environment and can be run using the command,

#### Installation

```bash
cd bot python -m venv ./venv && source ./venv/bin/activate
```

This command should be run inside the folder named “bot”. Doing so should activate the Python virtual environment. Now we need to install all the required Python packages. This can be done using the command,

```bash
pip install -r req.txt
```

By running the above command all the required packages should be installed and the bot can be run.

To run the bot we need to run the flask server built into it. To do that we need to run the command,

```bash
flask run
```

and that should run the flask server on the terminal and the chatbot should be accessible via the HTTP address shown on the terminal.

### Website

The website is a simple HTML website built using a JavaScript framework called Vue, this was because was the convenience of setting up a quick website for demonstration purposes. The website contains a built-in serve to help run it as well and all configurations have been made for the website to communicate with the chatbot.

The data for the website is a simple JSON list of objects that is hard-coded into the website and does not include any external data sources. The website simply provides an interface for the user to input messages and view the response of the chatbot.

#### Installation

To run the website’s built-in web server, we need to run the command,

```bash
npm run development
```

This will spin up the server and the website much like the chatbot server should be accessible through the web address shown on the terminal window.

This command should be done within the “chat” folder.

It was observed that, creating a rule-based chatbot requires a lot of work. Depending on the duties that a chatbot is expected to perform in a corporate setting, a lot more intent may be necessary.

Rule-based chatbots become completely unusable in this scenario since maintaining a rule basis would be exceedingly difficult. In addition, as it is very difficult to predict exactly how a user would engage with the bot, the chatbot's conversational skills would be severely constrained. Chatbots powered by AI are a far more useful answer for real-world situations.

## License

This software is open-sourced software licensed under the [MIT](LICENSE.md).

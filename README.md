GRAMMAR GIRAFFE, YOUR LANGUAGE ASSISTANT BOT.

Grammar Giraffe is a friendly language assistant Discord bot designed to enhance your linguistic experience. Whether you need to fetch meanings, correct sentences,fetch the word of the day,play a vocab game or simply have a good laugh with jokes and quotes, Grammar Giraffe is here to assist you.


## Table of Contents

- Features
- Commands
- Installation
- Usage
- Contributing
- License

## Features

Grammar Giraffe offers a variety of language-related features, including:

- **Meaning Retrieval:** Fetch the meanings of words using a vocabulary API.

- **Grammar Correction:** Correct grammar and spelling mistakes in sentences.

- **Flash Quizzes:** Engage in vocabulary quizzes to enhance your word knowledge.

- **Jokes:** Enjoy a good laugh with programming and dark humor jokes.

- **Quotes:** Get inspired with motivational quotes.

- **Word of the Day:** Discover a new word every day with its definition.You can also check the word of the day for a specific day.

## Commands

Grammar Giraffe supports several commands to interact with its features:

- `!intro`: Introduction to Grammar Giraffe, your language companion.

- `!hello`: Greeting from Grammar Giraffe.

- `!how are you today`: Check how Grammar Giraffe is feeling today.

- `!goodbye`: Bid farewell to Grammar Giraffe.

- `!thank you`: Express gratitude to Grammar Giraffe.

- `!help`: Display a list of available commands and their descriptions.

- `!meaning <word>`: Fetch the meaning of a specific word.

- `!check <sentence>`: Correct spelling and grammar in a sentence.

- `!flash`: Participate in vocabulary flash quizzes.

- `!joke`: Get a programming or dark humor joke.

- `!quotes`: Receive a motivational quote.

- `!wotd`: Discover the Word of the Day and its definition.

## Installation

To add Grammar Giraffe to your Discord server, follow these steps:

1. Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications).

2. Clone this GitHub repository to your local machine or server.

3. Install the required Python packages using `pip install -r requirements.txt`.

4. Set up your bot token and API keys for dictionary and joke services in the code (remember to keep them secure).

5. Run the bot using `python grammar_giraffe_bot.py`.

6. Invite the bot to your Discord server by providing the OAuth2 URL generated in the Developer Portal.

## Usage

- Type any of the supported commands mentioned in the (##commands) section to interact with Grammar Giraffe.

- Follow the bot's responses to navigate its features effectively.

## Contributing

If you'd like to contribute to Grammar Giraffe, please follow these steps:

1. Fork this repository.

2. Create a new branch for your changes.

3. Make your desired changes and improvements.

4. Test your changes thoroughly.

5. Submit a pull request with a clear description of your contribution.

## Troubleshooting

- **Bot Not Responding:**
  If the bot does not respond within a reasonable time (e.g., 3 seconds), it might indicate an issue with the input. Double-check your command syntax and input and try again. If the problem persists, it's possible that an error has occurred in the bot's operation.

  In case of repeated issues, consider reviewing the bot's logs or error messages for more details on what went wrong. If you suspect a bug or need assistance, feel free to let me know about it.

## Important Note Regarding the !joke Command.

Occasionally, you may encounter a situation where the `!joke` command initially prints a 'single ' instead of a complete joke. Rest assured, this is a known behavior and not a bug.

The `!joke` command fetches jokes from various sources, and sometimes it may receive incomplete or partial data. In such cases, the bot will display the received content, which may appear as a single word or phrase.

However, the bot will quickly follow up with a complete joke, when you type !joke again.t. If you don't see a complete joke within a few seconds, you can try the command again.

I apologize for any confusion this behavior may cause and appreciate your understanding.

## Note on Grammar Correction

Please note that the grammar correction feature provided by Grammar Giraffe is powered by various language processing tools and models. While it strives to provide accurate grammar corrections, it may not always be perfect.

Grammar correction algorithms, like any automated tool, have limitations, and they may not fully capture the context or nuances of natural language. Therefore, it's recommended to use the suggested corrections as guidelines and exercise your own judgment.

If you encounter a situation where the grammar correction doesn't seem accurate or if you have any doubts, feel free to seek further clarification or consult additional grammar resources. Grammar Giraffe is here to assist you but may not always guarantee flawless corrections.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README template further to include additional information or sections that you find relevant to your bot and its users. Providing clear and concise documentation will make it easier for others to understand and use your Discord bot effectively.

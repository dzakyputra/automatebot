# automatebot

Read the full tutorial in my [medium](https://medium.freecodecamp.org/@dzakyputra)

Check the bot in [here](http://telegram.me/automatereportbot).

This bot will automate your reporting task by querying the data to bigquery, doing visualization, and automatically send the image through Telegram Chat.

### Requirements
- python 3
- [Google BigQuery](https://github.com/googleapis/google-cloud-python)
- [matplotlib](https://matplotlib.org/)
- [numpy](http://www.numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

### Steps
Install the libraries.
```
pip3 install google-cloud-bigquery matplotlib numpy pandas python-telegram-bot
```

Create a developer account to access Google BigQuery API, you can follow the "Getting Started" steps in [here](https://medium.freecodecamp.org/@dzakyputra)

Configure the path.
```
export GOOGLE_APPLICATION_CREDENTIALS='[PATH_TO_CREDS.JSON]'
```

Run the program.
```
python3 main.py
```

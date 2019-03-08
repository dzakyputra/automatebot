# automatebot

Read the full tutorial in my [medium](https://medium.freecodecamp.org/how-to-build-a-bot-to-automate-your-mindless-tasks-using-python-and-google-bigquery-a34faf7fb74)

Check the bot in [here](http://telegram.me/automatereportbot), type `/send` command to see the example of image visualization.

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

Create a developer account to access Google BigQuery API, you can follow the **Getting Started** steps in [here](https://medium.freecodecamp.org/how-to-build-a-bot-to-automate-your-mindless-tasks-using-python-and-google-bigquery-a34faf7fb74)

Configure the path.
```
export GOOGLE_APPLICATION_CREDENTIALS='[PATH_TO_CREDS.JSON]'
```

Run the program.
```
python3 main.py
```

### Edit
You can customize the query based on your needs.

```
query = """ 
            YOUR_QUERY_HERE
        """
```
You can also configure when the bot has to send the image visualization.

```
updater.job_queue.run_daily(send_image, time=datetime.datetime.strptime('YOUR_TIME', '%I:%M%p').time(), days=(0,1,2,3,4,5,6))
```

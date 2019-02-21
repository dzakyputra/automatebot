from google.cloud import bigquery
from telegram.ext import Updater

import matplotlib.pyplot as plt
import numpy as np
import datetime

def query_to_bigquery(query):
    client = bigquery.Client()
    query_job = client.query(query)
    result = query_job.result()
    dataframe = result.to_dataframe()
    return dataframe

def visualize_bar_chart(x, x_label, y, y_label, title):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    index = np.arange(len(x))
    plt.xticks(index, x, fontsize=5, rotation=30)
    plt.bar(index, y)
    return plt

def get_and_save_image():
    query = """ 
                SELECT DATE(creation_date) date, COUNT(*) total_posts
                FROM `bigquery-public-data.stackoverflow.post_history`
                GROUP BY 1
                HAVING date > DATE_SUB('2018-12-02', INTERVAL 14 DAY)
                ORDER BY 1
            """
    dataframe = query_to_bigquery(query)   
    x = dataframe['date'].tolist()
    y = dataframe['total_posts'].tolist()
    plt = visualize_bar_chart(x=x, x_label='Date', y=y, y_label='Total Posts', title='Daily Posts')
    plt.savefig('viz.png')

def send_image(bot, update):
    get_and_save_image()
    chat_id = '216993313'
    bot.send_photo(chat_id=chat_id, photo=open('viz.png', 'rb'))

def main():
    updater = Updater('731229543:AAE2DTuVEBXg9tKVHEob78NHatfa5ADZgBY')
    updater.job_queue.run_daily(send_image, time=datetime.datetime.strptime('9:00AM', '%I:%M%p').time(), days=(0,1,2,3,4,5,6))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import requests
import csv
import json
import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timedelta


# importing coin_symbol2id assets
def get_coin_symbol2id():
    # check cache
    try:
        with open("data/coin_symbol2id.csv", 'r', newline='') as f:
            reader = csv.reader(f)
            coin_symbol2id = {rows[0]:rows[1] for rows in f}
    except BaseException:
        coin_symbol2id = dict()

    # renew data assets
    if len(coin_symbol2id) < 100:
        coin_symbol2id = dict()
        url = "http://api.coincap.io/v2/assets?limit=2000"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        json_assets = json.loads(response.text.encode('utf8'))

        coin_symbol2id = dict()

        for entry in json_assets["data"]:
            coin_symbol2id[entry['symbol']] = entry['id']
        
        # write cache
        with open("data/coin_symbol2id.csv", 'w', newline='') as out:
            writer = csv.writer(out)
            for key in coin_symbol2id.keys():
                out.write(f"{key},{coin_symbol2id[key]}\n")
    
    return coin_symbol2id

coin_symbol2id = get_coin_symbol2id()

# importing data on asset and date
def get_coin_price(coin_symbol='BTC', 
                   start=dt.strftime(dt.today().date() - timedelta(days=30), format = '%Y-%m-%d'),
                   end=dt.strftime(dt.today().date(), format = '%Y-%m-%d')):

    start_unix = int(dt.strptime(start, '%Y-%m-%d').timestamp())
    end_unix = int(dt.strptime(end, '%Y-%m-%d').timestamp())

    if coin_symbol is None:
        coin_symbol = ''
    coin_id = coin_symbol2id[coin_symbol]

    const_url = "http://api.coincap.io/v2/assets/"
    custom_url = f"{coin_id}/history?interval=d1&start={start_unix}000&end={end_unix}000"
    url = const_url + custom_url

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text.encode('utf8'))

    # save data
    coin_data = json_data["data"]

    # store to df
    df = pd.DataFrame(coin_data)
    df = df.drop('time', axis=1)
    df['priceUsd'] = df['priceUsd'].astype(float)
    df.date = pd.to_datetime(df['date'], format='%Y-%m-%dT%H:%M:%S.%fZ')

    return df
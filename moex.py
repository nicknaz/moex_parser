import requests

import apimoex
import pandas as pd


with requests.Session() as session:
    data = apimoex.get_board_candles(session, 'MVID', 60)
    df = pd.DataFrame(data)
    #df.set_index('TRADEDATE', inplace=True)
    print(df.tail(10))
    print(df.tail(10)['close'], '\n')
    df.info()
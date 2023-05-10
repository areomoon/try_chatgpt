from chatgpt_wrapper import ChatGPT
import pandas as pd
import time


def batch(iterable, b_size=1):
    total_len = len(iterable)
    for ndx in range(0, total_len, b_size):
        yield iterable[ndx: min(ndx + b_size, total_len)]


df = pd.read_csv('to_chatgpt_2.csv')
batch_size = 10
prompt = " corrected words as entities in Singapore: "

keywords = df['keyword'].unique().tolist()[181:]
bot = ChatGPT()

responses = []
for idx, kw in enumerate(batch(keywords, b_size=batch_size)):
    kw_l = '\n'.join(kw)
    response = bot.ask(f"{prompt} {kw_l} ")
    while 'Unusable response produced' in response:
        print('add')
        time.sleep(5)
        response = bot.ask(f"{prompt} {kw_l} ")
    responses.append(response)
    print(response)

df['chatgpt_query_correction'] = responses
# df.to_csv('chatgpt_query_correction.csv', index=False)
from requests import get
import datetime
import pandas as pd
import os


ip = get('https://api.ipify.org').text

now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M')

df = pd.DataFrame(data = [[current_time, ip]])

# Running this script in ubuntu workbench
os.chdir('/home/ubuntu/Desktop')
df.to_csv('ip_address.csv', mode='a', header=False, index=False)

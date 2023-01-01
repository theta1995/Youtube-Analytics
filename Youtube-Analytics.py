import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv() #Load enviroment variables
API_KEY = os.getenv("API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")


service = build("youtube", "v3", developerKey=API_KEY)

request = service.channels().list(
    part="statistics",
    id=CHANNEL_ID
)

channel = request.execute()
channelStatistics = channel['items'][0].get('statistics')

print(f"View Count: {channelStatistics['viewCount']}")
print(f"Subscribers Count: {channelStatistics['subscriberCount']}")
print(f"Videos Count: {channelStatistics['videoCount']}")

service.close()

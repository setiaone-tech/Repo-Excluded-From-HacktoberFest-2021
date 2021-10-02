import configparser
import json
import asyncio

import csv
import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)

# Reading Configs
config = configparser.ConfigParser()
config.read("telegram_config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

async def main(phone):
    await client.start()
    print("Client Created")

    # Ensuring you're authorized or not
    if await client.is_user_authorized() == False:
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    # enter the telegram channel invite link
    user_input_channel = input("enter entity(telegram URL or entity id):")
    
    if user_input_channel.isdigit():
        entity = PeerChannel(int(user_input_channel))
    else:
        entity = user_input_channel

    my_channel = await client.get_entity(entity)

    offset = 0
    limit = 100
    all_participants = []
    
    while True:
        participants = await client( GetParticipantsRequest( my_channel, ChannelParticipantsSearch(''), offset, limit, hash=0 ))
        
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset += len(participants.users)

    all_user_details = []
    for participant in all_participants:
        all_user_details.append(
                                    {"id": participant.id, 
                                    "first_name": participant.first_name, 
                                    "last_name": participant.last_name,
                                    "user": participant.username, 
                                    "phone": participant.phone, 
                                    "is_bot": participant.bot
                                    }
                                )

    # Writing the data to json file
    with open('user_data.json', 'w') as outfile:
        json.dump(all_user_details, outfile)

    with open('user_data.json') as json_file: 
        data = json.load(json_file) 

    # Opening the csv file to write the data in it from json file
    data_file = open('data_file.csv', 'w') 
    csv_writer = csv.writer(data_file) 

    # Writing the names of columns in csv file
    headers = ["id","Name","Last Name","Username","Phone number","IsBot"]
    csv_writer.writerow(headers)

    for item in data :
        id=item['id']
        first_name = str(item['first_name']).encode(errors='ignore')
        last_name = str(item['last_name']).encode(errors='ignore')
        username = str(item['user']).encode(errors='ignore')
        phone_number = str(item['phone'])
        isBot = item['is_bot']

        row = [id,first_name,last_name,username,phone_number,isBot]
        
        # Writing the data to the csv file
        csv_writer.writerow(row)
    
    data_file.close()

with client:
    client.loop.run_until_complete(main(phone))
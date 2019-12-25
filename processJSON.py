import json
import pandas as pd
import codecs
import sys
import os
import argparse
import logging



parser = argparse.ArgumentParser(description='Process instagam message.json files to csv')
parser.add_argument('--f', help='filepath to the JSON messages.json downladed from instagram',required=True)
parser.add_argument('--u', help='Your usename',required=True)
parser.add_argument('--v', help='Verbose',default=logging.INFO)

logger = logging.getLogger('process logger')

args = parser.parse_args()

logger.setLevel(int(args.v))
username = args.u
filename = args.f


def processJSON(filename,username):
    conversations={}
    with codecs.open(filename, encoding = 'utf-8', errors = 'ignore') as f:
        data = json.load(f)
        ctr = 1
        count = 1
        for participants in data:
            p = participants['participants']
            try:
                p.remove(username)
            except:
                logger.warning("Invalid username")
                sys.exit(0)
            p = ' '.join(p)
            conversation = conversations.get(p, [])
            c = participants['conversation']
            for message in c:
                author = message['sender']
                date = pd.to_datetime(message['created_at']).strftime('%Y/%m/%d %H:%M:%S')
                if('text' in message):
                    content = message['text']
                elif('media_url' in message):
                    content = '<media>'
                elif('animated_media_images' in message):
                    content  = '<animated_media>'
                conversation.append([date, author, content])
            conversations[p] = conversation


    if not os.path.exists('data'):
        os.makedirs('data')
    for conversation in conversations.keys():
        logger.info(f"Saving conversation for f{conversation}")
        pd.DataFrame(conversations[conversation],columns=['Date','Author','Message']).to_csv(f'data/{conversation}.csv')
            
if __name__ == "__main__":
    logger.info("Starting processing")
    processJSON(filename,username)
    logger.info("Finished processing")
            
from CNUCSECrawling import *
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open('Crawling\index.json', encoding="UTF-8") as f:
    json_data = json.loads(f.read())
a =json.dumps(json_data['late'], ensure_ascii=False)

print(type(a))
from pymongo import MongoClient
from pprint import pprint


client = MongoClient('localhost', 27017)
db = client['instagram']
users = db.instagram

name = input('Введите имя пользователя: ')
subscriber = users.count_documents({'$and': [{'username': name, 'user_type': 'follower'}]})
print(f'-------------------\nПОДПИСЧИКИ: {subscriber}\n-------------------')
for user in users.find({'$and': [{'username': name, 'user_type': 'follower'}]}):
    pprint(user)
subscription = users.count_documents({'$and': [{'username': name, 'user_type': 'following'}]})
print(f'-------------------\nПОДПИСКИ: {subscription}\n------------------- ')
for user in users.find({'$and': [{'username': name, 'user_type': 'following'}]}):
    pprint(user)
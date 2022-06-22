from pymongo import MongoClient


client: MongoClient = MongoClient()

account = {'name': 'Uemerson Pinheiro Junior'}
client.db.account.insert_one(account)

# pymongo add _id to account dictionary
print(account)

print('_id' in account)
# output: True

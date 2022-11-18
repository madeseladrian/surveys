import mongomock
import uuid

myclient = mongomock.MongoClient()
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"name": "Mades", "email": "mades.eladrian@gmail.com", "password": "123456"}

x = mycol.insert_one(mydict)

mades = mycol.find_one({"email": "mades.eladrian@gmail.com"})

mades['id'] = str(mades['_id'])
mades.pop('_id')

updated = mycol.update_one({}, {"$set": {'access_token': str(uuid.uuid4())}})

mades = mycol.find_one({"email": "mades.eladrian@gmail.com"})
print(f'Mades: {mades}')

# Created by kor_a at 08/08/2021
import pymongo
from pymongo import MongoClient

#Client
client = MongoClient('localhost', 27017)

#print all databases
print(client.list_database_names())

#connect to a database
db = client.cheatsheet

#show collections in database
#print(db.list_collection_names())

#Show documents in collection ('test' for example)
#print(db.test.count_documents({}))

#find and print docs
#cursor = db.test.find({})

#print docs
#for doc in cursor:
#    print(doc)

#find one doc
#db.test.find_one({'key' : value})


#find with list
#db['test'].find_one({'key' : value})


#create collection
#db.create_collection('test2')

#insert data
#db.test2.insert_one({'name' : 'testt'})

#insert many data
#db.test.insert_many([
#    {'name' : 'orkun'},
#    {'name' : 'koray'},
#])


#update docs one and many

# just one orkun updated
#db.test.update_one(
#    {'name' : 'orkun'},                         #search
#    { '$set' : {'name' : 'gungor'}}             #update
#)

# all orkun's are updated
#db.test.update_many(
#    {'name': 'orkun'},                          #search
#    {'$set': {'name': 'gungor'}}                #update
#)


#create new document called salaryinfo

#init_sal = 100000
#for val in range(10):
#    db.salaryinfo.insert_many([
#        {'name' : 'orkun'},
#        {'Salary' : init_sal}
#    ])

# get salary which is > 150000
#query_result = db.salaryinfo.find({'Salary' : { '$gt' : 150000} })

#show
#for doc in query_result:
#    print(doc)

#update many salary
#db.salaryinfo.update_many(
#    {'Salary' : {'$gt' : 150000}},
#    {'$set': {'Salary' : 175000}}
#)

# and or condition
#query_result = db.salaryinfo.find(
#    { '$and' : [{ 'Salary' : { '$gt' : 100000}}, { 'Salary' : { '$lt' }}]}
#)







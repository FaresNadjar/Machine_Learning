# Create Database
In MongoDB, a database is not created until it gets content, so if this is your first time creating a database, you should complete the next two chapters (create collection and create document) before you check if the database exists!
```python3
myclient = pymongo.MongoClient(\mongodb://localhost:27017/\)

#Create a database called \mydatabase\:
mydb = myclient[\mydatabase\]

#Check if a database exist by listing all databases in you system:
print(myclient.list_database_names())

#Check a specific database by name, Check if \mydatabase\ exists::
dblist = myclient.list_database_names()
if \mydatabase\ in dblist:
print(\The database exists.\)
```
# Create Collection
A collection in MongoDB is the same as a table in SQL databases.

In MongoDB, a collection is not created until it gets content, so if this is your first time creating a collection, you should complete the next chapter (create document) before you check if the collection exists!
```python3
#Create a collection called \customers\ inside mydb:
mycol = mydb[\customers\]

#Return a list of all collections in your database:
print(mydb.list_collection_names())

#Check if the \customers\ collection exists:
collist = mydb.list_collection_names()
if \customers\ in collist:
print(\The collection exists.\)
```
# Insert Document
A document in MongoDB is the same as a record in SQL databases.
```python3
#Let's insert a record in the \customers\ collection:
mydict = { \name\: \John\, \address\: \Highway 37\ } #We create a dictionnaire
x = mycol.insert_one(mydict) #We insert it

#Insert another record in the \customers\ collection, and return the value of the _id field:
#If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
mydict = { \name\: \Peter\, \address\: \Lowstreet 27\ }
x = mycol.insert_one(mydict)
print(x.inserted_id)

#To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
mylist = [
{ \name\: \Amy\, \address\: \Apple st 652\},
{ \name\: \Hannah\, \address\: \Mountain 21\},
{ \name\: \Michael\, \address\: \Valley 345\},
{ \name\: \Sandy\, \address\: \Ocean blvd 2\},
{ \name\: \Betty\, \address\: \Green Grass 1\},
{ \name\: \Richard\, \address\: \Sky st 331\},
{ \name\: \Susan\, \address\: \One way 98\},
{ \name\: \Vicky\, \address\: \Yellow Garden 2\},
{ \name\: \Ben\, \address\: \Park Lane 38\},
{ \name\: \William\, \address\: \Central st 954\},
{ \name\: \Chuck\, \address\: \Main Road 989\},
{ \name\: \Viola\, \address\: \Sideway 1633\}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)

#If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert
#the document(s). Remember that the values has to be unique. Two documents cannot have the same _id.
mylist = [
{ \_id\: 1, \name\: \John\, \address\: \Highway 37\},
{ \_id\: 2, \name\: \Peter\, \address\: \Lowstreet 27\},
{ \_id\: 3, \name\: \Amy\, \address\: \Apple st 652\},
{ \_id\: 4, \name\: \Hannah\, \address\: \Mountain 21\},
{ \_id\: 5, \name\: \Michael\, \address\: \Valley 345\},
{ \_id\: 6, \name\: \Sandy\, \address\: \Ocean blvd 2\},
{ \_id\: 7, \name\: \Betty\, \address\: \Green Grass 1\},
{ \_id\: 8, \name\: \Richard\, \address\: \Sky st 331\},
{ \_id\: 9, \name\: \Susan\, \address\: \One way 98\},
{ \_id\: 10, \name\: \Vicky\, \address\: \Yellow Garden 2\},
{ \_id\: 11, \name\: \Ben\, \address\: \Park Lane 38\},
{ \_id\: 12, \name\: \William\, \address\: \Central st 954\},
{ \_id\: 13, \name\: \Chuck\, \address\: \Main Road 989\},
{ \_id\: 14, \name\: \Viola\, \address\: \Sideway 1633\}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
```
# Find
In MongoDB we use the find and findOne methods to find data in a collection.

Just like the SELECT statement is used to find data in a table in a MySQL database.

No parameters in the find() method gives you the same result as SELECT * in MySQL.
```python3
#Find the first document in the customers collection:
x = mycol.find_one()
print(x)
print('####')

#Return all documents in the \customers\ collection, and print each document:
for x in mycol.find():
print(x)
print('####')

#Return only the names and addresses, not the _ids:
#You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
#If you specify a field with the value 0, all other fields get the value 1, and vice versa:
for x in mycol.find({},{ \_id\: 0, \name\: 1, \address\: 1 }):
print(x)
print('####')

#This example will exclude \address\ from the result:
for x in mycol.find({},{ \address\: 0 }):
print(x)
print('####')

#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in mycol.find({},{ \name\: 1, \address\: 0 }):
print(x)
```
# Query
When finding documents in a collection, you can filter the result by using a query object.

The first argument of the find() method is a query object, and is used to limit the search.
```python3
#Find document(s) with the address \Park Lane 38\:
myquery = { \address\: \Park Lane 38\ }
mydoc = mycol.find(myquery)
for x in mydoc:
print(x)
print('####')

#To make advanced queries you can use modifiers as values in the query object.
#E.g. to find the documents where the \address\ field starts with the letter \S\ 
#or higher (alphabetically), use the greater than modifier: {\$gt\: \S\}:
myquery = { \address\: { \$gt\: \S\ } }
mydoc = mycol.find(myquery)
for x in mydoc:
print(x)
print('####')

#Regular expressions can only be used to query strings.
#Find documents where the address starts with the letter \S\:
myquery = { \address\: { \$regex\: \^S\ } }
mydoc = mycol.find(myquery)
for x in mydoc:
print(x)
print('####')
```
# Sort
Use the sort() method to sort the result in ascending or descending order.
    
The sort() method takes one parameter for \fieldname\ and one parameter for \direction\ (ascending is the default direction).
```python3
    #Sort the result alphabetically by name:
    mydoc = mycol.find().sort(\name\)
    for x in mydoc:
        print(x)
    print('####')
    #sort(\name\, 1) #ascending
    #sort(\name\, -1) #descending
    #Sort the result reverse alphabetically by name:
    mydoc = mycol.find().sort(\name\, -1)
    for x in mydoc:
        print(x)
```
# Delete Document
To delete one document, we use the delete_one() method.

The first parameter of the delete_one() method is a query object defining which document to delete.

Note: If the query finds more than one document, only the first occurrence is deleted.

To delete more than one document, use the delete_many() method.

The first parameter of the delete_many() method is a query object defining which documents to delete.

To delete all documents in a collection, pass an empty query object to the delete_many() method.
```python3
#Delete the document with the address \Mountain 21\:
myquery = { \address\: \Mountain 21\ }
mycol.delete_one(myquery)

#Delete all documents were the address starts with the letter S:
myquery = { \address\: {\$regex\: \^S\} }
x = mycol.delete_many(myquery)
print(x.deleted_count, \ documents deleted.\)
print('####')

#Delete all documents in the \customers\ collection:
x = mycol.delete_many({})
print(x.deleted_count, \ documents deleted.\)
```
# Drop Collection
You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
```python3
#Delete the \customers\ collection:
mycol.drop()
```
# Update
You can update a record, or document as it is called in MongoDB, by using the update_one() method.

The first parameter of the update_one() method is a query object defining which document to update.

Note: If the query finds more than one record, only the first occurrence is updated.

The second parameter is an object defining the new values of the document.

To update all documents that meets the criteria of the query, use the update_many() method.
```python3
#Change the address from \Valley 345\ to \Canyon 123\:
myquery = { \address\: \Valley 345\ }
newvalues = { \$set\: { \address\: \Canyon 123\ } }
mycol.update_one(myquery, newvalues)
#print \customers\ after the update:
for x in mycol.find():
print(x)
print('####')

#Update all documents where the address starts with the letter \S\:
myquery = { \address\: { \$regex\: \^S\ } }
newvalues = { \$set\: { \name\: \Minnie\ } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, \documents updated.\)
```
# Limit
To limit the result in MongoDB, we use the limit() method.

The limit() method takes one parameter, a number defining how many documents to return.
```python3
#Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
print(x)
```
# Create Index will allows to optimize search requests 
```python3
collection.create_index({seasonId:1, teamId:1, competitionId:1})
```

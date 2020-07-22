# Useful ressources :

- One hot Encoding : https://hackernoon.com/what-is-one-hot-encoding-why-and-when-do-you-have-to-use-it-e3c6186d008f?gi=a4f47cf027f7

## Pickle

It is used for serializing and de-serializing a Python object structure. Any object in python can be pickled so that it can be saved on disk. What pickle does is that it “serialises” the object first before writing it to file. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.

Pickle has two main methods. The first one is dump, which dumps an object to a file object and the second one is load, which loads an object from a file object.

```python
# Import Pickle
import pickle

# Let's prepare a list to serialize for example :
a = ['test value', 'test value 2', 'test value 3']

# To better understant how to use open
# https://www.w3schools.com/python/ref_func_open.asp
# create a file for writing :
file_Name = "testfile"
fileObject = open(file_Name, 'wb') #wb for write

# Dump the object a serialized in the file created :
pickle.dump(a, fileObject)

# Close the fileObject
fileObject.close()

# Now we reopen fileObject but with a reading mode
fileObject = open(file_Name,'rb') 

# load the object from the file into var b
b = pickle.load(fileObject)

# Let's test if a == b
a==b
```

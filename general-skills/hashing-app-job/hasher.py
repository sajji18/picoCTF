
# importing the required libraries
import hashlib

# making a message
inputstring = input()

# encoding the message using the library function
output = hashlib.md5(inputstring.encode())

# printing the hash function
print(output.hexdigest())

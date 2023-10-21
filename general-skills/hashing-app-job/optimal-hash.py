import hashlib
from pwn import *
import re

# what it does is it simply generates the md5 hash given a string
def generateMD5Hash(new_word): 
    md5hash = hashlib.md5(new_word.encode()).hexdigest()
    return md5hash

def main():
	# here we are using the remote function of pwntools to 
    # connect to the server saturn.picoctf.net on port 52679.
    conn = remote('saturn.picoctf.net', 52679)
    # challenge variable, initiated here and it will later on have the challenge
    challenge = ""
    # While loop to interact with the server by send and receiving messages until
    # a certain condition is met, if that never occurs it is an infinite loop (while True)
    while True:
    	# try is required because recv line could throw and exception 
    	# and we want to catch it if it does.
        try:
	        # conn.recvline() is going to receive a line from the server and 
			# store it on the variable serverOutput
            serverOutput = conn.recvline()
            # If the variable serverOutput has the string Incorrect, it means
            # that the generateMD5Hash is wrong, therefore I print out (to 
			# myself) fix the code!! XD and I break the loop, line 30.
            if 'Incorrect.' in serverOutput.decode():
                print("Wrong hash. Fix the code!! ")
                break
            # If the variable serverOutput has the string Answer, it means
            # we have to send an answer to the server, the hashing of the 
            # string keyword, in this case the challenge is in the 2nd 
            # position of the variable challenge (initiated before)
            elif 'Answer:' in serverOutput.decode():
                conn.send((generateMD5Hash(challenge[1]) + '\n').encode())
            If the variable serverOutput has the string Answer, it means
            # If the variable serverOutput has the string picoCTF{, it means
            # we have found the flag!! We have the solution, and what I do is 
            # simply get it from the serverOutput variable and print it out 
            # to the user
            elif 'picoCTF{' in serverOutput.decode():
                flag = re.findall('picoCTF{.*}', serverOutput.decode())
                print("The flag is: " + flag[0])
                break
            # If the variable serverOutput has the string ' it means
            # we have the challenge message to hash later, what I do is
            # I simply store it in the variable challenge, to be called
            # later in the iteration of the loop, once the word Answer is 
            # in the serverOutput (line 35)
            elif "'" in serverOutput.decode():
                challenge = serverOutput.decode().split("'")
            else:
                continue
        except EOFError as e:
            print(e)

main()

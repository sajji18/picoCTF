# Script for Covnerting ascii values to characters

# Using absolute path
with open('E:/picoCTF/general-skills/Nice-netcat/nice-netcat.txt') as f:
    lines = f.readlines()
    
array = []

for line in lines:
    asc_val = chr(int(line))
    array.append(asc_val)
    
# print(flag)

flag = ''.join(array)
print(flag)
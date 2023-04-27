
import hashlib,glob
import os

os.getcwd()

hashArray = []


for file in os.listdir("hash-files"):
        if file.endswith(".txt"):
            with open(os.path.join("hash-files", file), 'rb') as f:
                print(file)
                contents = f.read()
                hash=hashlib.sha1(contents).hexdigest()
                hashArray.append(hash)

print("Hashvalues:")
print(hashArray)

if(len(hashArray)%2!=0):
    hashArray.append(hashArray[-1])
while(len(hashArray)>1):
    j=0
    for i in range(0, len(hashArray)-1):
        f = str(hashArray[i]+hashArray[i+1])
        hashArray[j]=hashlib.sha1(f.encode()).hexdigest()

        i+=2
        j+=1
    del hashArray[j:]
#Recompute top Hash
if (len(hashArray)==1):
    print("The top Hash:")
    print(hashArray)
    with open("check.aap", "a") as a:
         a.write(hashArray[0])
    print("The Top Hash saved in check.aap")   


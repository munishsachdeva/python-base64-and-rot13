#In Fristileaks vulnhub
#Step 1) takes string and encodes it to base64
#Step 2) [::-1] reverses order of the chars in string
#Step 3) rot13 encodes the string

#Now replace code by
import base64,codecs,sys
def encodeString(str):
    decoded = codecs.decode(str[::-1], 'rot13')
    return base64.b64decode(decoded)
cryptoResult=encodeString(sys.argv[1])
print (cryptoResult)

#Run as python 


from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import socket
import pickle

#setup socket
host = socket.gethostname()
conn2 = socket.socket()
port2 = 1234
conn2.connect((host, port2))


#import private key
encryptedPrivateKey= open("aliceprivate.dat","r").read()
privateKey = RSA.import_key(encryptedPrivateKey)

#import public key
encryptedPublicKey= open("alicepublic.dat","r").read()
publicKey = RSA.import_key(encryptedPublicKey)



message = "Lets wash our hands every hour"#create a message
message = message.encode('utf-8')
hashMessage = int.from_bytes(SHA256.new(message).digest(), byteorder = 'big')#create hash message
signature = pow(hashMessage, privateKey.d, privateKey.n)# create alice signature
messageToSend = (message, hashMessage, signature)# define how a message is setup
a = {1: message, 2:hashMessage, 3:signature}#create a message with pickle
msg = pickle.dumps(a)#format message
conn2.sendall(msg)#send message
conn2.close()

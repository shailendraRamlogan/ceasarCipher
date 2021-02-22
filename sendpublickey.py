from Crypto.PublicKey import RSA
import socket
#setup socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345



conn.bind((host, port))
conn.listen(1)

#read public key
encryptedPublicKey = open("alicepublic.dat","r").read()
publicKey = RSA.import_key(encryptedPublicKey)
publicKey = publicKey.exportKey().decode()

s, addr = conn.accept()
s.send(publicKey.encode('utf-8'))#send public key
print('PublicKey Sent')
s.close()

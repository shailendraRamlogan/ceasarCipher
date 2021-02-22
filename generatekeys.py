from Crypto.PublicKey import RSA
from Crypto import Random


randomKey = Random.new().read
privateKey = RSA.generate(2048, randomKey)#create private key
encryptedPrivateKey = privateKey.exportKey()
publicKey =privateKey.publickey()#create public key
encryptedPublicKey = publicKey.exportKey()

privateFile = open("aliceprivate.dat", "w")#save private key
privateFile.write(encryptedPrivateKey.decode())

publicFile = open("alicepublic.dat", "w")#save public key
publicFile.write(encryptedPublicKey.decode())

privateFile.close()
publicFile.close()

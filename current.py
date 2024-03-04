from Crypto.Cipher import AES

key   = b"TheNeuralNineKey"
nonce = b"TheNeuralNineKNce"

cipher = AES.new(key,AES.MODE_EAX,nonce)
ciphertext = cipher.encrypt(b"Code Alpha Task-4")
print(ciphertext)

cipher = AES.new(key,AES.MODE_EAX,nonce)
print(cipher.decrypt(ciphertext))
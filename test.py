from AES_hybrid import *
import time
import base64

with open("googlefooter.png", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

start_time = time.time()
enc = AES()

encry = enc.encrypt_cbc('ahdfsujeytsbsdfawskdfhsdgfereijd', my_string)
print("time for encryption --- %s seconds ---" % (time.time() - start_time))
with open("encry_test_Img.enc", "wb") as img_file:
    img_file.write(encry)

start_time2 = time.time()
decry = enc.decrypt_cbc('ahdfsujeytsbsdfawskdfhsdgfereijd', encry)
print("time for decryption --- %s seconds ---" % (time.time() - start_time2))
with open("out_test_Img.jpeg", "wb") as img_file:
    img_file.write(base64.b64decode(decry))

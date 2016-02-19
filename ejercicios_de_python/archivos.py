import string
import random

ar = open("archivo.txt", "wb")

ar.write("Esta es una prueba de escritura en un archivo .txt\n")
for i in range(100):
	texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
	ar.write("%s\n" % texto)

ar.close()

ar = open("archivo.txt", "r+")
srti = ar.read()

print srti

ar.close()
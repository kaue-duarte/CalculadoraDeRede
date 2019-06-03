#coding=utf-8



def DecBin(decimal):
	lista = []

	if decimal>= 128:
		decimal = decimal-128
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 64:
		decimal = decimal-64
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 32:
		decimal = decimal-32
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 16:
		decimal = decimal-16
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 8:
		decimal = decimal-8
		lista.append (int(1))
	else:
		lista.append (int(0))
	
	if decimal>= 4:
		decimal = decimal-4
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 2:
		decimal = decimal-2
		lista.append (int(1))
	else:
		lista.append (int(0))

	if decimal>= 1:
		decimal = decimal-1
		lista.append (int(1))
	else:
		lista.append (int(0))

	return lista


octeto1 = DecBin(int (input("Informe o 1o octeto: ")))
octeto2 = DecBin(int (input("Informe o 2o octeto: ")))
octeto3 = DecBin(int (input("Informe o 3o octeto: ")))
octeto4 = DecBin(int (input("Informe o 4o octeto: ")))

masc = int(input("Informe a mascara: "))

print "A mascara e: ", masc


def BinDec(octeto):
	a = oct11 = oct12 = oct13 = oct14 = oct15 = oct16 = oct17 = oct18 = 0

	if octeto[7] == 1:
		oct11 = a+1
		
	if octeto[6] == 1:
		oct12 = a+2

	if octeto[5] == 1:
		oct13 = a+4

	if octeto[4] == 1:
		oct14 = a+8
		
	if octeto[3] == 1:
		oct15 = a+16
	   
	if octeto[2] == 1:
		oct16 = a+32
		
	if octeto[1] == 1:
		oct17 = a+64

	if octeto[0] == 1:
		oct18 = a+128

	return oct11+oct12+oct13+oct14+oct15+oct16+oct17+oct18

octeto2a = octeto2
octeto3a = octeto3
octeto4a = octeto4
if masc == 8:
	if [1] * 8 != octeto2 and [0] * 8 != octeto2:
		print "E endereco de host: ", BinDec(octeto1), BinDec(octeto2), BinDec(octeto3), BinDec(octeto4)

	print "Endereco de rede: ", BinDec(octeto1), BinDec([0] * 8), BinDec([0] * 8), BinDec([0] * 8)
	print "Endereco de broadcast: ", BinDec(octeto1), BinDec([1] * 8), BinDec([1] * 8), BinDec([1] * 8)

if masc == 9:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 7 != octeto2[1:] and [0] * 7 != octeto2[1:]: 
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	for i in range(1,7):
		octeto2a[i] = 0
	
	octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	for i in range(1,7):
		octeto2a[i] = 1
	
	octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4
if masc == 10:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 6 != octeto2[2:] and [0] * 6 != octeto2[2:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2


	for i in range(2,7):
		octeto2a[i] = 0
	
	octeto2a[2:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	for i in range(2,7):
		octeto2a[i] = 1
	
	octeto2a[2:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 11:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 5 != octeto2[3:] and [0] * 5 != octeto2[3:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(3,7):
		octeto2a[i] = 0
	
	octeto2a[3:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(3,7):
		octeto2a[i] = 1
	
	octeto2a[3:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4


if masc == 12:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 4 != octeto2[4:] and [0] * 4 != octeto2[4:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(4,7):
		octeto2a[i] = 0
	
	octeto2a[4:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(4,7):
		octeto2a[i] = 1
	
	octeto2a[4:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 13:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 3 != octeto2[5:] and [0] * 3 != octeto2[5:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4


	octeto2a = octeto2

	for i in range(5,7):
		octeto2a[i] = 0
	
	octeto2a[5:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(5,7):
		octeto2a[i] = 1
	
	octeto2a[5:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4
	
if masc == 14:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 2 != octeto2[6:] and [0] * 2 != octeto2[6:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4
	octeto2a = octeto2

	for i in range(6,7):
		octeto2a[i] = 0
	
	octeto2a[6:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4
	
	octeto2a = octeto2

	for i in range(6,7):
		octeto2a[i] = 1
	
	octeto2a[6:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 15:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 1 != octeto2[7:] and [0] * 1 != octeto2[7:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto2a = octeto2

	for i in range(7,7):
		octeto2a[i] = 0
	
	octeto2a[7:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	for i in range(7,7):
		octeto2a[i] = 1
	
	octeto2a[7:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2a)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 16:
	octeto3a = octeto3
	octeto4a = octeto4
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 8 != octeto3 and [0] * 8 != octeto3:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4
	
	octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 17:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 7 != octeto3[1:] and [0] * 7 != octeto3[1:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4
	octeto3a = octeto3
	
	for i in range(1,7):
		octeto3a[i] = 0

	octeto2a[1:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(1,7):
		octeto3a[i] = 1

	octeto2a[1:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 18:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 6 != octeto3[2:] and [0] * 6 != octeto3[2:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4
	octeto3a = octeto3
	
	for i in range(2,7):
		octeto3a[i] = 0

	octeto2a[2:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(2,7):
		octeto3a[i] = 1

	octeto2a[2:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 19:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 5 != octeto3[3:] and [0] * 5 != octeto3[3:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(3,7):
		octeto3a[i] = 0

	octeto2a[3:] = octeto3aocteto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(3,7):
		octeto3a[i] = 1

	octeto2a[3:] = octeto3aocteto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 20:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 4 != octeto3[4:] and [0] * 4 != octeto3[4:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4
	octeto3a = octeto3
	
	for i in range(4,7):
		octeto3a[i] = 0

	octeto2a[4:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(4,7):
		octeto3a[i] = 1

	octeto2a[4:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4
if masc == 21:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 3 != octeto3[5:] and [0] * 3 != octeto3[5:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(5,7):
		octeto3a[i] = 0

	octeto2a[5:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(5,7):
		octeto3a[i] = 1

	octeto2a[5:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 22:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 2 != octeto3[6:] and [0] * 2 != octeto3[6:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(6,7):
		octeto3a[i] = 0

	octeto2a[6:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(6,7):
		octeto3a[i] = 1

	octeto2a[6:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 23:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 1 != octeto3[7:] and [0] * 1 != octeto3[7:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(7,7):
		octeto3a[i] = 0

	octeto2a[7:] = octeto3a = octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto3a = octeto3
	
	for i in range(8,8):
		octeto3a[i] = 1

	octeto2a[7:] = octeto3a = octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", octeto1, octeto2, octeto3a, octeto4a

if masc == 24:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	if [1] * 8 != octeto4 and [0] * 8 != octeto4:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4
	
	octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3a)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 25:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 7 != octeto4[1:] and [0] * 7 != octeto4[1:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4


	octeto4a[1:] = octeto4
	
	for i in range(1,7):
		octeto4a[i] = 0

	octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(1,7):
		octeto4a[i] = 1

	octeto4a[1:] = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 26:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 6 != octeto4[2:] and [0] * 6 != octeto4[2:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4


	octeto4a = octeto4
	
	for i in range(2,7):
		octeto4a[i] = 0

	octeto4a[3:] = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(2,7):
		octeto4a[i] = 1

	octeto4a[3:] = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 27:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 5 != octeto4[3:] and [0] * 5 != octeto4[3:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(3,7):
		octeto4a[i] = 0

	octeto4a[4:] = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(3,7):
		octeto4a[i] = 1

	octeto4a[4:] = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4
	
if masc == 28:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 4 != octeto4[4:] and [0] * 4 != octeto4[4:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(4,7):
		octeto4a[i] = 0

	octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(4,7):
		octeto4a[i] = 1

	octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 29:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 3 != octeto4[5:] and [0] * 3 != octeto4[5:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(5,7):
		octeto4a[i] = 0

	octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(5,7):
		octeto4a[i] = 1

	octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 30:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 2 != octeto4[6:] and [0] * 2 != octeto4[6:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(6,7):
		octeto4a[i] = 0

	octeto4a = [0] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(6,7):
		octeto4a[i] = 1

	octeto4a = [1] * 8
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4

if masc == 31:
	conv1 = BinDec(octeto1)
	conv2 = BinDec(octeto2)
	conv3 = BinDec(octeto3)
	conv4 = BinDec(octeto4a)
	if [1] * 1 != octeto4[7:] and [0] * 1 != octeto4[7:]:
		print "E endereco de host: ", conv1, conv2, conv3, conv4
	else:
		print "E endereco de rede"

	octeto4a = octeto4
	
	for i in range(7,7):
		octeto4a[i] = 0

	octeto4a = [0] * 8
	conv4 = BinDec(octeto4a)
	print "Endereco de rede: ", conv1, conv2, conv3, conv4

	octeto4a = octeto4
	
	for i in range(7,7):
		octeto4a[i] = 1

	octeto4a = [1] * 8
	conv4 = BinDec(octeto4a)
	print "Endereco de broadcast: ", conv1, conv2, conv3, conv4


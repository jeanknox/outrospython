from Crypto.Hash import SHA256
while True:
	chave= input("digite o valor a ser calculada a chave SHA256:")
	h= SHA256.new()
	h.update(chave)
	print chave.hexdigest()

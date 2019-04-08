usuarios={jean:00336a9537dc3269125a009b4fd802beda8beccd920e517513577bc162830cee}
`
def crypto():
    from Crypto.Hash import SHA256
    c = SHA256.new()
    print c.hexdigest()
crypto(jean)
while True:
    usuario=("Digite um nome de usuario")
    if usuario in usuarios:
        senha=("Digite a senha deste usuario")
    if usuario not in usuarios:
        print("Digite a senha para o usuario[]".format(usuario))
    usuarios[usuario]= senha
from Crypto.Hash import SHA256
h = SHA256.new()
while True:
    chave=str(input(b"Digite o valor a ser codificado:"))

h.update(chave)
    print h.hexdigest()

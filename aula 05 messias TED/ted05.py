amigos = ["Leticia", "Eduardo", "Diogo", "Pedro"]

saudacao = "Eae, como você está, {}?"

for amigos in amigos:
    mensagem = saudacao.format(amigos)
    print(mensagem)
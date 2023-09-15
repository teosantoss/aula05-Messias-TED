# Lista de convidados para uma sesh em minha residência.
lista_convidados = ["Matuê", "Teto", "Kanye West", "Tz", "Snoop Dog"]

# Mensagem de convite.
mensagem_convite = "Você está sendo convidado para participar da sesh!"

# Convites para cada pessoa da lista.
for convidado in lista_convidados:
    print(f"Enviando convite para {convidado}...")
    print(mensagem_convite)

# Quem não pode comparecer.
nao_pode_comparecer = "Tz"

# Nome da celebridade que não poderá comparecer!
print(f"\n{nao_pode_comparecer} não pode comparecer a sesh. \n")

# Substituindo os desistentes por novas Celebridades.
lista_convidados.remove(nao_pode_comparecer)
novo_convidado = "Mc Ryan"
lista_convidados.append(novo_convidado)

# Enviando novos convites para as pessoas que continuam na lista
for convidado in lista_convidados:
    print(f"Enviando novo convite {convidado}...")
    print(mensagem_convite)
# forma obsoleta
nome = 'Fulano'
idade = 40
profissao = 'dev'
linguagem = 'Python'

print("olá, meu nome é %s. Minha idade é %d anos. Minha profissão é %s de %s." % (nome, idade, profissao, linguagem))

#método format
nome = 'Fulano'
idade = 40
profissao = 'dev'
linguagem = 'Python'
  #dicionário
pessoa = {"nome":'Fulano',"idade":40,"profissao": 'dev', "linguagem":'python'}
print("olá, meu nome é {}. Minha idade é {} anos. Minha profissão é {} de {}.".format(nome, idade, profissao, linguagem))

print("olá, meu nome é {3}. Minha idade é {2} anos. Minha profissão é {1} de {0}.".format(linguagem, profissao, idade, nome))

print("olá, meu nome é {nome}. Minha idade é {idade} anos. Minha profissão é {profissao} de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao,linguagem=linguagem))

print("olá, meu nome é {nome}. Minha idade é {idade} anos. Minha profissão é {profissao} de {linguagem}.".format(**pessoa))

#metodo f-string
nome = 'Fulano'
idade = 40
profissao = 'dev'
linguagem = 'Python'

print(f"F-STRING: olá, meu nome é {nome}. Minha idade é {idade} anos. Minha profissão é {profissao} de {linguagem}.")

#FORMATAR STRINGS COM F-STRING
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")#com largura
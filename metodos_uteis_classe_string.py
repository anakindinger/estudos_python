palavra = "pYthon"

print(palavra.upper())
#transforma todas os caracteres em maiúsculo

print(palavra.lower())
#transforma todas os caracteres em minúsculo

print(palavra.title())
# primeiro caracter em maiúsculos

print(palavra.strip())
#retira espaços em branco do início e fim da string

print(palavra.lstrip())
#retira espaço em branco do início da string

print(palavra.rstrip())
#retira espaço em branco do fim da string

print(palavra.center(10,'#'))
#centraliza a string entre um número igual de caracteres pre-definidos (#) dentro do limite definido (10)

print(".".join(palavra))
#funciona com todos os tipos iteráveis e adiciona a instrução do join a cada iteração


# 38) Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.
cod_correto = 1234
senha_correta = 9999
senha = 0

print("Digite seu codigo:")
cod = int(input())

if cod != cod_correto:
    print("Usuario invalido!")
else:
    print("Digite sua senha:")
    senha = int(input())
    
if senha != senha_correta:
    print("Senha incorreta!")
else:
    print("Acesso permitido!")

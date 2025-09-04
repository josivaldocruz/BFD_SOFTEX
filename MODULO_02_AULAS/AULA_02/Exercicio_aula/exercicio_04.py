# Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir).
# Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.


try:
    abrirarquivo = open("dados.txt,r")
    abrirarquivo.read()

    abrirarquivo.close
except:print("Arquivo não existe")

finally:
    print("Encerrando programa")
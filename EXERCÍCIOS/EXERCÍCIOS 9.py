import random

numero = random.randint(1,50)

for computador in range (5):
    num = int(input("Diite um valor: "))
    if num == numero:
        print("Acertou")
        break
    elif num > numero:
        print("Tente novamente, seu número é maior")
    elif num < numero:
        print("Teste novamente, seu número é menor")
    
if(erro == 1 ): 
    print ("O número sortiado foi: ", numero)
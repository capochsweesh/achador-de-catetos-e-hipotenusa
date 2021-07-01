import math

def main():

    escolha = str(input('Qual lado do triângulo você quer saber? (Oposto, Hipotenusa ou Ajacente) ')).strip().lower()
    if escolha == 'adjacente':
        get_cat_adjacente()
    elif escolha == 'hipotenusa':
        get_hipo()
    elif escolha == 'oposto':
        get_cat_oposto()

def get_hipo():

    cateto1 = float(input('Digite o Cateto Oposto: '))
    cateto2 = float(input('Digite o Cateto Adjacente: '))
    hipotenusa = math.hypot(cateto1,cateto2)
    print('A hipotenusa de {} e {} é {:.2f}'.format(cateto1,cateto2,hipotenusa))

def get_cat_adjacente():
    
    cateto1 = float(input('Digite o Cateto Oposto: '))
    hipotenusa = float(input('Digite a Hipotenusa: '))
    cateto2 = hipotenusa**2 - cateto1**2
    print('O Cateto Adjacente do Cateto Oposto {} e da Hipotenusa {} é {:.2f}'.format(cateto1,hipotenusa,math.sqrt(cateto2)))
    
def get_cat_oposto():

    cateto2 = float(input('Digite o Cateto Adjacente: '))
    hipotenusa = float(input('Digite a Hipotenusa: '))
    cateto1 = hipotenusa**2 - cateto2**2
    print('O Cateto Oposto do Cateto Adjacente {} e da Hipotenusa {} é {:.2f}'.format(cateto2,hipotenusa,math.sqrt(cateto1)))

             
if __name__ == "__main__":
    main()
    

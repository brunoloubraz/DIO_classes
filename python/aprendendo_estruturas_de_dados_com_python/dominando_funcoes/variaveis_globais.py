# salario = 2000

# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     return salario

# print(salario_bonus(500))

    # ''' 
    # TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
    #      para obtenção dos valores.
    # TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
    #      aproveitar ao máximo a oferta.
    # '''



# print(int(7/4))

T = int(input())

for i in range(T):
    n, k = map(int, input().split())
    total = (n // k) + (n % k)
    print(total)


    #     ''' 
    # TODO Crie as condições necessárias para definir o tipo de animal possível seguindo
    # o esquema da imagem.
    # TODO Imprima, de acordo com as condições, o animal identificado.
    # '''
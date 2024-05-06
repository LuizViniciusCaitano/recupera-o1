n1 = int(input("Digite o primeiro numero:\n"))
n2 = int(input("Digite o segundo numero:\n"))
n3 = int(input("Digite o terceiro numero:\n"))

if n1 != n2 and n1!= n3 and n2 !=n3:
    if n1 < n2 and n1 < n3 and n2 < n3:
        print(n1, n2, n3)
    elif n1 < n2 and n1 < n3 and n3 < n2:
        print(n1, n3, n2)
    elif n2 < n1 and n2 < n3 and n1 < n3:
        print(n2, n1, n3)
    elif n2 < n1 and n2 < n3 and n1 < n3:
        print(n2, n3, n1)
    elif n3 < n2 and n3 < n1 and n1 < n2:
        print(n3, n1, n2)
    elif n3 < n2 and n3 < n1 and n2 < n1:
        print(n3, n2, n1) 
def proxima():
    while True:
        choose = input("Quer virar mais uma carta? (S/N): \n").upper()
        if choose == 'S':
            return True
        elif choose == 'N':
            return False
        else:
            print('Opção inválida!')

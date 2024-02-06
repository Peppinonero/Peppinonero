def Numeri():
    numList = []
    print('Inserisci fino a 7 numeri. Premi solo invio per terminare prima.')
    for i in range(7):
        numInput = input(f"Inserisci il numero {i+1} (o premi invio per terminare): ")
        if numInput == '':
            break
        try:
            num = int(numInput)
            numList.append(num)
        except ValueError:
            print("Per favore, inserisci un numero valido.")
            break
    return numList

def Ordinamento(numList):
    if numList == sorted(numList):
        return "La lista è ordinata in modo crescente."
    elif numList == sorted(numList, reverse=True):
        return "La lista è ordinata in modo decrescente."
    else:
        return print("La lista non è ordinata. Te la ordino io", sorted(numList)) 
        

def Somma(numList):
    return sum(numList)

def Massimo(numList):
    return max(numList)

def main():
    numList = Numeri()
    if not numList:
        print("Nessun numero inserito.")
    else:
        print(Ordinamento(numList))
        print("La somma dei numeri è:", Somma(numList))
        print("Il numero più grande è:", Massimo(numList))

if __name__ == "__main__":
    main()
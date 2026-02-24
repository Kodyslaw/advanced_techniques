#stwórz funckcję obliczającą średnią artytmetyczną z listy liczb
#dodaj type hints



lista =[10,210,33,21,60] #definicja listy 
def srednia(lista) -> float: #type hint to "wskazówka" na to jaki typ wartości jest oczekiwany
    if len(lista) == 0: #check czy lista jest pusta
        return 0 
    suma = sum(lista) #suma liczb
    srednia = suma / len(lista) #dzielenie sumy przez ilość liczb w liście
    return srednia 
print(srednia(lista))
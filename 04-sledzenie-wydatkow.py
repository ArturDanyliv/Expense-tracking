from cmath import exp

global expense_month
expenses = [] #tworzymy liste wydatkow

def show_expenses(month):   #wyswietlac te wydatki #tutaj tez potrzebujemy month-mieiac 
    #bo bedziemy wyswietlac dla pojedynczego miesiaca 
    
        #print(expenses)  #albo wyswietlic wszystko co dodalismy
        
        for expense_amount,expense_type,epense_month in expenses: #wyswietlic tylko wydatki z danego miesiaca petla for 
    # expense_month - miesiac ktory bedzie pochodzil z tych krotek ktore mamy na liscie expenses 
    # month - to miesiac o ktorego pyta uzytkownik
            if expense_month == month :                   #wyswietlic tylko wydatki danego miesiaca
                print(f'{expense_amount} - {expense_type}')  #tworzymy stringa do jakiego mozna wrzucic zmienne 




def add_expense(month):     #musimy zaimplementowac tą funkcje 
    print()                 # i tutaj bedziemy dodawac wydatek
    expense_amount = int(input("Podaj kwote [zł] : "))    #zapytamy uzytkownika o kwote tego wydatku
    expense_type =input("Podaj typ wydatku(jedzenie,rozrywka,dom,inny) : ")        #typ wydatku

    expense = (expense_amount,expense_type,month)        
    #tworzymy ten wydatek  #sklada sie z expense_amount,type,month

    expenses.append(expenses) #dodalismy wydatek do naszej listy

def show_expenses(month):                    #zdefiniujemy funkcje dla  show_stats
    total_amount_this_month = sum(expense_amount for expense_amount, _ ,epense_month in expenses if expense_month == month)
    #i sumowac wszystkie wydatki   #wyliczenia wszystkich wydatkow w danym miesiacu 
    #przejsc przez cała liste i wziac wszystkie wydatki z obiektu
    #chcemy wziac expense_amount tylko wtedy kiedy dotyczy to danego miesiąca 
    #expense_amount + expense_amount
    #epense_month in expenses #jest taki sam epense_month jak i month
    # sprawdzenie czy ten wydatek dotyczy miesiąca o który pytamy dla tego jest if expense_month == month
    
    number_of_expense_this_month = sum(1 for _ , _ ,epense_month in expenses if expense_month == month)
    #SREDNIE WYDATKI W DANYM MIESIACU DO TEGO POTRZEUJEMY INFORMACJE ILE WYDATKOW WOGOLE MIELISMY W DANYM MIESIACU 
    #kazdy wydatek to jest jeden pojedynczy wydatek jezeli sobie dodamy wszystkie jedynki wtedy otrzymamy liczbe wszystkicj 
    #zamiast expense_amount mamy 1
    #za kazdym razem 1+1+1 kiedy wnaszej liscie wydatkow expense_month == month
    
    average_expense_this_month = total_amount_this_month / number_of_expense_this_month
    #dzielimy cała kwote przez liczbe wydatków i dzieki temu mamy sredni wydatek 

    total_amount_all = sum(expense_amount for expense_amount, _ , _ in expenses ) 

    average_expense_all = total_amount_all / len(expenses)                                #sredni wydatek ogolnie
    #pdzielic zalkowita sume przez liczbe wydatków
    #liczba wydatkow to  len () - dlugosc to zwraca dlugosc listy   #lista wydatkow to expenses


    print()
    print["Statystyki "]
    print("Wszystkie wydatki w tym miesiącu [zł] :",total_amount_this_month) #musimy to wszystko dodac do siebe dla tego bierzemy wyrazenie expense
    print("Sredni wydatek w tym miesiącu [zl] : ",average_expense_this_month)
    print("Wszystkie wydatki [zł] : ",total_amount_all)
    print("Sredni wydatek [zł] : ",average_expense_all)





from random import choices


while True:           #petla nieskonczona while True
    print()
    month=int(input("Wybierz miesiąc [1-12]:")) #jesli to bedzie liczba calkowita potrzeujemy int(....)

    if month == 0:       #kiedy uzytkownik oda 0 miesiac konczy dzialanie naszej apikacji 
        break        #i wychodzimy z pętli while

    while True:     #petla nieskonczona zeby uzytkownik wybierał miesiąc :dostępne opcje
        print()
        print("0.Powrót do wybory miesiaca")
        print("1.Wyswietl wszystkie wydatki")
        print("2.Dodaj wydatek")
        print("3.Statystyki ")
        choice = int(input("Wybierz opcje :"))    #zapisac wyvor uzytkownika  no i int bo liczba

        if choice == 0:          #jezeli wybor bedzie 0
            break 

        if choice == 1:                #powrot do pierwszego meni
            #print("Wszystkie wydatki")
            show_expenses(month)

        if choice == 2:
            print("Dodaj wydatki")
            add_expense(month)
        
        if choice == 3:
            #print("Twoje statytyki")
            #show_stats = ()
            show_expenses(month)
            


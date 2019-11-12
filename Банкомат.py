cash=1000
attempts=3
password='1234'
pin=''
while pin != password and attempts >0:
    print('Введи пин-код:')
    print('У вас ' + str(attempts) + ' попытки')
    attempts -=1
    pin=input()
if pin==password:
    print('Пароль верен')
    print("Добро пожаловать вы зашли!")
    while True:
        print("Что вы желаете делать?(1-Баланс,2-положить деньги,3-снять деньги 4-выйти)")
        t=input()
        if t=="3":
            print("Сколько хотите снять: ")
            e=int(input())
            if e<=int(cash):
                d=cash-int(e)
                print("У вас осталось на счету:" + str(d))
            else:
                print("Недостаточно средств!")
        elif t=='4':  
            print('Ну пока')
            break
        elif t=='1':
            print("На счету:" + str(cash))
        else:
            print("Сколько хотите положить: ")
            r=int(input())
            m=r+cash
            print('Теперь у тебя на счету ' + str(m))
else:
    print('Попытки кончились, карточка заблокирована')
import random
drow=0
win=0
lose=0
times=int(input('Игра Каменьножницыбумага. Сколько раз хотите играть? '))
for i in range(times):
    choice=[1,2,3]
    bot=random.choice(choice)
    user=int(input('Выбери Камень(1), Ножницы(2), Бумага(3) '))
    if bot==user:
        print('Ничья, тебе повезло, кожаный уб...')
        drow+=1
    elif user==1 and bot==2:
        print('Победа!')
        win+=1
    elif user==2 and bot==3:
        print('Победа!')
        win+=1
    elif user==3 and bot==1:
        print('Победа!')
        win+=1
    elif user==2 and bot==1:
        print('Поражение!')
        lose+=1
    elif user==3 and bot==2:
        print('Поражение!')
        lose+=1
    elif user==1 and bot==3:
        print('Поражение')
        lose+=1
    else:
        print('Создатель дебил')
    print('Компьютор выбрал', bot)
    answer=input('Хотите продолжить играть?(Y/N)')
    if answer=='N':
        break
print('Победы ',win,'Поражения ',lose, 'Ничьи ', drow)

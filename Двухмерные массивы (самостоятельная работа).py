#The first task
import random as r#импорт рандома как r

max=0
a=[]
n=int(input('Strings: '))#n - строки, m - столбцы
m=int(input('Elements: '))#задаём переменные(и список) по условию

for i in range(n):
    a.append([r.randint(1,9) for j in range(m)])#добавляем элементы в список (в столбец) с помощью рандома


for i in range(n):
    for j in range(m):
        if max<a[i][j]:#ищем максимум
            max=a[i][j]

print('The first biggest number is', max, '\nThe string of number is', i, '\nThe index of number is', j)#выводим

#The second task
n=int(input('Write side of square: '))#задаём переменные(и список) по условию
if n%2==0:n+=1#Если задали чётное число, делаем его нечётным
a=[['.']*n for i in range(n)]#заполняем список символом '.'

for i in range(n):#задаём условия, по которым будет расстравлен знак "*"
    for j in range(n):
        if i==j or (n-j==i+1):
            a[i][j]='*'
        if i==n//2:
            a[i][j]='*'
        if j==n//2:
            a[i][j]='*'


for i in range(len(a)):#выводим не как список
    print()
    for j in range(len(a[i])):
        print(a[i][j], end=' ')

#The third task
n=int(input('Strings: '))
m=int(input('Column: '))#задаём переменные(и список) по условию
a=[['.']*m for i in range(n)]#заполняем список символом '.'


for i in range (n):
    for j in range(m):
        if (i%2!=0 and j%2==0) or (i%2==0 and j%2!=0):#задаём условия, по которым будет расстравлен знак "*"
            a[i][j]='*'

for i in range(len(a)):#выводим не как список
    print()
    for j in range(len(a[i])):
        print(a[i][j], end=' ')

#The fouth task
n=int(input('Write side of square: '))
a=[[0]*n for i in range(n)]#заполняем список цифрой 0
z=1#переменная, которая будет число, на которое заменяют, и условием

while z!=n:#создаём цикл
    for i in range(n):#задаём условия, по которым будут расставлены цифры
        for j in range(n):
            if i==j-z or i==j+z: 
                a[i][j]=z

    if n-1==i and n-1==j:# когда for прошёл по всему списку добавляем к z 1 
        z+=1

for i in range(len(a)):#выводим не как список
    print()
    for j in range(len(a[i])):
        print(a[i][j], end=' ')

#The fifth task
n=int(input('Write side of square: '))
a=[[1]*n for i in range(n)]#заполняем список цифрой 1

for i in range(n):
    for j in range(0,i):#заполняем список в одном диапазоне цифрой 2
        a[i][j]=2
    for j in range(i+1,n):##заполняем список в другом диапазоне цифрой 0
        a[i][j]=0


for i in range(len(a)):#выводим не как список
    print()
    for j in range(len(a[i])):
        print(a[i][j], end=' ')

#The sixth task
n=int(input('Strings: '))
m=int(input('Column: '))
a=[[0]*m for i in range(n)]#задаём переменные(и список) по условию

for ii in range(n):
    for jj in range(m):
        a[ii][jj]=input('Write {1} element of {0} string: '.format(ii+1,jj+1))#задаём элементы
        
i=int(input('Write сolumn you want to replace: '))
j=int(input('Write сolumn you want to be replace: '))#задаём какие колонны нужно поменять местами

for ii in range(n):
    a[ii][i],a[ii][j] = a[ii][j],a[ii][i] #меняем колонны местами
          
for ii in range(len(a)):#выводим не как список
    print()
    for jj in range(len(a[ii])):
        print(a[ii][jj], end=' ')

#The seventh task
n,m=[int(i) for i in input('Write number of strings and columns: ').split()]#задаём переменные по условию

a=[[m*i+j+1 if i%2==0 else m*(i+1)-j for j in range(m)] for i in range (n)]#cортируем список по условию

for x in a:
    print(' '.join([str(a) for a in x]))#выодим не как список
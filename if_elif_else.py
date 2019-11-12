#task1
a=int(input('Please write meaning of  first number: '))
b=int(input('Please write meaning of second number: '))
if a<b:
    print(b, ': b является больше')
elif b<a:
    print(a, ': a является больше')
else:
    print(a,'равно',b)
#task2
x=int(input('Please write meaning of x: '))
if x>0:
    sign=1#sing(x)
elif x<0:
    sign=-1#sing(x)
else:
   sign=0#sing(x)
print('sign(x) is',sign)
#task3
a1=int(input('Choose first column: '))
a2=int(input('Choose first string: '))
b1=int(input('Choose second string: '))
b2=int(input('Choose second column:: '))
if (a1+b1+a2+b2)%2==0:
    print('YES, they have one colour')
else:
    print('NO, they haven\'t one colour')
#task4
year=int(input('Please write number of year: '))
if year%4==0 and (year%100!=0 or year%400==0):
    print('Year is ')
else:
    print('Year isn\'t ')
#task5
a=int(input('Please write first number '))
b=int(input('Please write second number '))
c=int(input('Please write third number '))
if a<b and a<c:
    print('Lower number is a', a)
elif b<a and b<c:
    print('Lower number is b', b)
elif c<b and c<a:
    print('Lower number is c', c)
else:
    print('Lower numbers are some')
#task6
a=int(input('Please write first number '))
b=int(input('Please write second number '))
c=int(input('Please write third number '))
if a==b and b==c:
    print('3, all numbers are same')
elif a==b or b==c or a==c:
    print('2, two numbers are same')
else:
    print('0, no one namber are same')
#task7
a1=int(input('Choose first column: '))
a2=int(input('Choose first string: '))
b1=int(input('Choose second string: '))
b2=int(input('Choose second column:: '))
if a1==b1 or a2==b2:
    print('Yes')
else:
    print('No')
#task8
x1=int(input('Choose first column: '))
y1=int(input('Choose first string: '))
x2=int(input('Choose second string: '))
y2=int(input('Choose second column:: '))
if x1==x2 or y1==y2:
    print('Yes')
else:
    print('No')
#task9
x1=int(input('Choose first column: '))
y1=int(input('Choose first string: '))
x2=int(input('Choose second string: '))
y2=int(input('Choose second column:: '))
if abs(x1-x2)==(y1-y2):
    print('Yes')
else:
    print('No')
#task10
x1=int(input('Choose first column: '))
y1=int(input('Choose first string: '))
x2=int(input('Choose second string: '))
y2=int(input('Choose second column:: '))
if abs(x1-x2)==(y1-y2) and (x1==x2 or y1==y2):
    print('Yes')
else:
    print('No')
#task11
x1=int(input('Choose first column: '))
y1=int(input('Choose first string: '))
x2=int(input('Choose second string: '))
y2=int(input('Choose second column:: '))
if (abs(x1-x1==2) and abs(y1-y2==1)) or (abs(x1-x1==1) and abs(y1-y2==2)):
    print('Yes')
else:
    print('No')
#task12
n=int(input('Choose length: '))
m=int(input('Choose width: '))
k=int(input('Choose amount lobules: '))
if (n*m)>k and ((k%n==0) or (k%m==0)
    print('Yes')
else:
    print('No')
#task1
string=input('Write string: ')
#1
print('Сначала выведите третий символ этой строки.', string[2])
#2
print('Во второй строке выведите предпоследний символ этой строки.',string[-2])
#3
print('В третьей строке выведите первые пять символов этой строки.',string[0:6])
#4
print('В четвертой строке выведите всю строку, кроме последних двух символов.', string[0:-2])
#5
print('В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).', string[0::2])
#6
print('В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.', string[1::2])
#7
print('В седьмой строке выведите все символы в обратном порядке.', string[-1::0])
#8
print('В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.', string[-1:0:2])
#9
print('В девятой строке выведите длину данной строки', len(string)
#task2
string=input('Write string: ')
print(string.count(' ', 0, len(string))+1)
#task3
string=input('Write string: ')
print(string[(int((len(string))//2)):-1]+string[0:int((len(string)//2))])
#task4
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)
#taks5
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
#task6
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
#task7
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#task8
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)
#task9
print(input().replace('1', 'one'))
#task10
print(input().replace('@', ''))
#task11
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
#task12
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
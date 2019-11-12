f=open('input.txt', 'r')
#a=f.readlines()
a=f.readlines()
print(a)
f.close
#file out
fout=open('output.txt', 'w')
print('Hello world', file=fout)
#
with open('D:\output.txt','w') as file_write:
    for nr in range(1,100):
        file_write.write(str(nr)+'\n')
#
import urllib.request
f=urllib.request.urlopen('http://clck.ru/Jtvyd.txt')
print (f.read().decode('utf-8'))
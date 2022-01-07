

import threading
import time
from random import choice

lock = threading.Lock()
temp =''
index = 0
path = '.ulol'
text = ''

def word_gen(seed:int = 10,isword:bool =  False)->str:

    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    lower_alpha = alphabet.split()
    upper_alpha = alphabet.upper().split()
    special_mark = '! " # $ % & ( ) * + , - . / : ; < = ? ! > = _  £ @ * % $ € ¥'.split()
    temp = ""

    for i in range(seed):
        temp += choice(lower_alpha)
        temp += choice(upper_alpha)
        if(not isword):
            temp += choice(special_mark)

    return temp

print(text)

def daemon()->None:
    global path,temp,lock
    lock.acquire()
    
    with open(path,'r+') as file:
        temp = file.read()

def writer()->None:

    global path,text,lock,index
    lock.acquire()

    i=0
    
    while index True:
        path = f'.{word_gen(seed = 5,isword = True)}'
        with open(path,'a+') as file:
            while i != 666:
                text = word_gen()
                print(text)
                file.write(text)
                i = i + 1
        i = 0
        index = index + 1

    lock.release()

daemon_thread = threading.Thread(target=daemon,daemon=True)
writer_thread = threading.Thread(target=writer)

writer_thread.start()
daemon_thread.start()

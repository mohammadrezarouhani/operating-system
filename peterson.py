from threading import Thread
from time import sleep
from unicodedata import name

flag=[False,False]
turn=0


def critical_section(process_num):
    print("process {} entered critical section".format(process_num))


def reminder_section(process_num):
    print("process {} entered reminder section\n".format(process_num))


def peterson(process_num):
    flag[process_num]=True
    j = (process_num+1)%2
    global turn 
    turn =j

    while True:
        while turn==j and flag[j]:
            pass

        critical_section(process_num)
        flag[process_num]=False
        reminder_section(process_num)
        sleep(2)


if __name__=='__main__':
    li=[]
    for i in range(0,2):
        li.append(Thread(target=peterson,args=(i,)))

    for i in li:
        i.start()
    
    for i in li:
        i.join()
    
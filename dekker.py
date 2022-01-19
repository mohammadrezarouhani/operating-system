from threading import Thread
from time import sleep
from unicodedata import name

turn=0


def critical_section(process_num):
    print("process {} entered critical section".format(process_num))


def reminder_section(process_num):
    print("process {} entered reminder section\n".format(process_num))


def dekker(process_num):
    j = (process_num+1)%2
    global turn 

    while True:
        while not turn==process_num:
            pass

        critical_section(process_num)
        turn=j
        reminder_section(process_num)
        sleep(2)



if __name__=='__main__':
    li=[]
    for i in range(0,2):
        li.append(Thread(target=dekker,args=(i,)))

    for i in li:
        i.start()
    
    for i in li:
        i.join()
    
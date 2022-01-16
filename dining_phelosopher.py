from threading import Thread,Semaphore
from time import sleep

N=5
table=Semaphore(N-1)
chop_stick=[Semaphore()for i in range(0,N)]


def eating(process_num,right,left):
    print("process {} is eating with chopstcick {} and {} ".format(process_num+1,right,left))
    sleep(2)


def thinking(process_num):
    print("process {} is thinking ".format(process_num+1))


def phelosopher(process_num):
    left=(process_num) % N
    right=(process_num+1)% N

    table.acquire()
    chop_stick[left].acquire()
    chop_stick[right].acquire()

    eating(process_num,right,left)

    chop_stick[left].release()
    chop_stick[right].release()
    table.release()

    thinking(process_num)
    
    
if __name__=='__main__':
    li=[]
    for i in range(0,N):
        li.append(Thread(target=phelosopher,args=(i,)))

    for i in li:
        i.start()

    for i in li:
        i.join()

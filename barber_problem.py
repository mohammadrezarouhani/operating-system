from threading import Semaphore, Thread,Lock
from time import sleep

free_table_count=4
customer_queue=[]

customer_ready=Semaphore(0)  # this will check if we have a customer or not 
barber_ready_lock=Lock()    # this will check if barber is busy or not 
waiting_room_lock=Lock()    # every customer process should enter the wating room one by one 



def barber():   # this method is for barber process (every time a customer is ready it will execute)
    global free_table_count

    while True:
        if not customer_queue : # if there is no cusomer int queue barber will going to sleep with customer_ready semaphore
            print("barber is sleeping")

        customer_ready.acquire()

        cust_id=customer_queue.pop(0) 
        print("customer {} entred barber room {} in queue".format(cust_id+1,len(customer_queue)))
        free_table_count+=1
        print("barber is cutting customer {} hair".format(cust_id+1))
        sleep(4)

        barber_ready_lock.release() # this says that to the customers the barber is free


def customer(customer_num):
    global free_table_count

    waiting_room_lock.acquire()

    if free_table_count>0: # if there is any free palace in waiting room the customer will seat 
        print("customer {} entered the waiting room ==> {} free table".format(customer_num+1,free_table_count-1))
        customer_queue.append(customer_num)
        free_table_count-=1
        waiting_room_lock.release()

        barber_ready_lock.acquire()
        customer_ready.release()

    else: # if there is no free room, the customer process will going out and the process will finished 
      waiting_room_lock.release()


if __name__=='__main__':
    customer_list=[]
    customer_count=int(input('enter the cutomer number:\n\t')) 

    barber=Thread(target=barber)
    barber.start()

    for cust in range(0,customer_count): # this create the customers process
        customer_list.append(Thread(target=customer,args=(cust,)))
    
    for cust in customer_list:
        cust.start()

    for cust in customer_list:
        cust.join()

    barber.join()
    
#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>

void* dekker();
void critical_sec();
void reminder_sec();
int turn=0;


int main(int argc, char **argv){
    pthread_t thread[2];
    int process[2];
    
    for(int i=0; i<2;i++){
        process[i]=i;
        pthread_create(&thread[i],NULL,dekker,(void *)&process[i]);
    }

    for(int j=0; j<2;j++){
        pthread_join(thread[j],NULL);
    }
    return 0;
}


void* dekker(void* i){
    int proc_num=*(int *)i;
    
    int j=(proc_num+1)%2;// it will give the other proc number
    
    while(true){
        sleep(2);
        while (turn!=proc_num);// if not the turn for current process it will trap in this while 
        
        // entering critical section
        critical_sec(proc_num);
        turn=j;

        //entering reminder section
        reminder_sec(proc_num);

    }
}


void critical_sec(int proc_num){
    printf("process %d entred the critical section\n",proc_num);
}


void reminder_sec(int proc_num){
    printf("process %d entred the reminder section\n\n",proc_num);
}

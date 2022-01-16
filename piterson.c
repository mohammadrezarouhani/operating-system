#include <stdio.h>
#include <pthread.h>
#include <stdbool.h>

void* dekker();
void critical_sec();
void reminder_sec();

int turn=0;
bool flag[2]={false,false};


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
    
    flag[proc_num]=true;
    int j=(proc_num+1)%2;// it will give the other proc number
    turn=j;

    while(true){
        sleep(2);

        while(turn==j && flag[j]);// it will looping until the other one exited from critical sec 

        //entering critical section
        critical_sec(proc_num);
        //

        flag[proc_num]=false;

        // entering reminder section
        reminder_sec(proc_num);
    }
}


void critical_sec(int proc_num){
    printf("process %d entred the critical section\n",proc_num);
}


void reminder_sec(int proc_num){
    printf("process %d entred the reminder section\n\n",proc_num);
}
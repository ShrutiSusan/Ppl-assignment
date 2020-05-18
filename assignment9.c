#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>
#include<unistd.h>
int hours=0;
int minutes=0;
int seconds=0;
pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER;
void * calculate_seconds(){
	pthread_mutex_lock(&mutex);
	if(seconds==60){
            minutes+=1;
            seconds=0;
        }
        pthread_mutex_unlock(&mutex);
        pthread_exit(NULL);
}
void *calculate_minutes(){
	pthread_mutex_lock(&mutex);
	if(minutes==60){
            hours+=1;
            minutes=0;
        }
        pthread_mutex_unlock(&mutex);
        pthread_exit(NULL);
}
void * calculate_hours(){
	pthread_mutex_lock(&mutex);
	if(hours==24){
            hours=0;
            minutes=0;
            seconds=0;
        }
        pthread_mutex_unlock(&mutex);
        pthread_exit(NULL);
}	
int main(){
	
	pthread_t id[3];
	while(1){
		system("clear");
		seconds++;
		pthread_create(&id[0],NULL,calculate_seconds,NULL);
		pthread_create(&id[1],NULL,calculate_minutes,NULL);
		pthread_create(&id[2],NULL,calculate_hours,NULL);
		//finish each of the threads	
		pthread_join(id[0],NULL);
		pthread_join(id[1],NULL);
		pthread_join(id[2],NULL);
		printf("%2d : %2d : %2d",hours,minutes,seconds);
		
		fflush(stdout);
		sleep(1);   
	}
	return 0;
}

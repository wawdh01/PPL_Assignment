#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
void* get_hours (void *timeinfo) {
	sleep (1);
	struct tm *time = (struct tm*)timeinfo;
	return (void*)&time->tm_hour;
	//return NULL;
}
void* get_minutes (void *timeinfo) {
	sleep(1);
	struct tm *time = (struct tm*)timeinfo;
	return (void*)&time->tm_min;
}
void* get_seconds (void *timeinfo) {
	sleep (1);
	struct tm *time = (struct tm*)timeinfo;
	return (void*)&time->tm_sec;
}
int main () {
	time_t rawtime;
	int *h, *m, *s;
	struct tm *timeinfo;
	while (1) {
		time (&rawtime);
		timeinfo = localtime (&rawtime);
		pthread_t thread_hour, thread_min, thread_sec;
		pthread_create(&thread_hour, NULL, get_hours, (void*)timeinfo);
		pthread_create(&thread_min, NULL, get_minutes, (void*)timeinfo);
		pthread_create(&thread_sec, NULL, get_seconds, (void*)timeinfo);
		pthread_join (thread_hour, (void*)&h);
		pthread_join (thread_min, (void*)&m);
		pthread_join (thread_sec, (void*)&s);
		system("clear");
		if (*h < 10) {
			printf("0%d:", *h);
		}
		else {
			printf("%d:", *h);
		}
		if (*m < 10) {
			printf("0%d:", *m);
		}
		else {
			printf("%d:", *m);
		}
		if (*s < 10) {
			printf("0%d\n", *s);
		}
		else {
			printf("%d\n", *s);
		}
	}
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "matrix.h"
#include "work_queue.h"

int work_queue_init(work_queue_t *queue, unsigned size) {
    if (size == 0) {
        return -1;
    }

    int err = pthread_mutex_init(&queue->mutex, NULL);
    if (err != 0) {
        fprintf(stderr, "pthread_mutex_init: %s\n", strerror(err));
        return -1;
    }
    err = pthread_cond_init(&queue->item_available, NULL);
    if (err != 0) {
        fprintf(stderr, "pthread_cond_init: %s\n", strerror(err));
        pthread_mutex_destroy(&queue->mutex);
        return -1;
    }
    err = pthread_cond_init(&queue->space_available, NULL);
    if (err != 0) {
        fprintf(stderr, "pthread_cond_init: %s\n", strerror(err));
        pthread_mutex_destroy(&queue->mutex);
        pthread_cond_destroy(&queue->item_available);
        return -1;
    }

    queue->buffer = malloc(size * sizeof(work_queue_item_t));
    if (queue->buffer == NULL) {
        perror("malloc");
        pthread_mutex_destroy(&queue->mutex);
        pthread_cond_destroy(&queue->item_available);
        pthread_cond_destroy(&queue->space_available);
        return -1;
    }

    queue->buf_read_idx = 0;
    queue->buf_write_idx = 0;
    queue->buf_len = 0;
    queue->buf_capacity = size;
    queue->shutdown = 0;
    return 0;
}

int work_queue_free(work_queue_t *queue) {
    free(queue->buffer);
    int ret_val = 0;
    int err;
    err = pthread_mutex_destroy(&queue->mutex);
    if (err != 0) {
        fprintf(stderr, "pthread_mutex_destroy: %s\n", strerror(err));
        ret_val = -1;
    }

    err = pthread_cond_destroy(&queue->item_available);
    if (err != 0) {
        fprintf(stderr, "pthread_cond_destroy: %s\n", strerror(err));
        ret_val = -1;
    }

    err = pthread_cond_destroy(&queue->space_available);
    if (err != 0) {
        fprintf(stderr, "pthread_cond_destroy: %s\n", strerror(err));
        ret_val = -1;
    }

    return ret_val;
}

int work_queue_put(work_queue_t *queue, work_queue_item_t *item) {
    pthread_mutex_lock(&queue->mutex); //locks mutex before starting
    while(queue->buf_len==queue->buf_capacity){ //ensures space in buffer by waiting
        pthread_cond_wait(&queue->space_available, &queue->mutex); 

        if (queue->shutdown){ // if the queue is being shutdown, unlock the mutex and return 1 indicating shutdown
            pthread_mutex_unlock(&queue->mutex);
            return 1;
        }
    }
    int idx = queue->buf_write_idx; //find index for new item and place in buffer then increment
    queue->buffer[idx] = *item;
    queue->buf_len++;
    queue->buf_write_idx = (idx + 1) % queue->buf_capacity; //moves pointer to write
    pthread_cond_signal(&queue->item_available); //signals item available and unlocks mutex
    pthread_mutex_unlock(&queue->mutex);
    return 0;
}


int work_queue_get(work_queue_t *queue, work_queue_item_t *dest) {
    pthread_mutex_lock(&queue->mutex); //locks mutex before starting
    while(queue->buf_len==0){ // waits until item is available 
        pthread_cond_wait(&queue->item_available, &queue->mutex);
        if(queue->shutdown){ // if the queue is being shutdown, unlock the mutex and return 1 indicating shutdown
            pthread_mutex_unlock(&queue->mutex);
            return -1;
        }
    }
    int read = queue->buf_read_idx; // finds index of item to read and gets it, then moves pointer
    *dest = queue->buffer[read];
    queue->buf_read_idx = (read + 1) % queue->buf_capacity;
    queue->buf_len--; //buffer decremented
    pthread_cond_signal(&queue->space_available); //signals space available and unlocks mutex
    pthread_mutex_unlock(&queue->mutex);
    return 0;
}


int work_queue_shut_down(work_queue_t *queue) {
    pthread_mutex_lock(&queue->mutex); // locks mutex
    queue->shutdown = 1; //shuts down queue
    pthread_cond_broadcast(&queue->item_available); //makes all threads available for items
    pthread_cond_broadcast(&queue->space_available); //makes all threads available for space
    pthread_mutex_unlock(&queue->mutex); //unlocks mutex
    return 0;
}

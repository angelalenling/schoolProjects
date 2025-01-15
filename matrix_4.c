#include <limits.h>
#include <math.h>
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "matrix.h"

typedef struct{ // custom struct definition with multiple args
    const matrix_t *mat; //pointer to matrix
    unsigned start; // starting row of the chunk for a thread
    unsigned end; // ending row of the chunk for a thread
    int result; // the result of this thread
}thread_arguments;

void *sum_result(void *args){ //thread function to compute sum
    thread_arguments *mat_data = (thread_arguments *)args; // single void * argument
    int *sum = malloc(sizeof(int));
    *sum = 0;
    for(int i = mat_data->start; i < mat_data->end; i++){ // iterates through matrix chunk
        for(int j = 0; j < mat_data->mat->ncols; j++){
            *sum += matrix_get(mat_data->mat, i, j); //updates sum
        }
    }
    return sum; // sum pointer as result of this function
}

void *max_result(void *args){ //thread function to find max
    thread_arguments *mat_data = (thread_arguments *)args; // single void * argument
    int *max = malloc(sizeof(int)); //temp max value memory allocation
    *max = 0;
    for(int i = mat_data->start; i < mat_data->end; i++){ // iterates through matrix chunk
        for(int j = 0; j < mat_data->mat->ncols; j++){
            int curr_val = matrix_get(mat_data->mat, i, j); // check current value to see if larger than temp max
            if(curr_val > *max){
                *max = curr_val; // updates the overall max
            }
        }
    }
    return max; // max pointer as result of this function
   
}

//sums the elements of multiple threads

int matrix_parallel_sum(const matrix_t *mat, unsigned n_threads, long *result) { 
    pthread_t threads[n_threads];
    thread_arguments thread_data[n_threads]; //neccessary data for each thread to operate
    int rows = floor(mat->nrows / (double)n_threads); //each thread processes this many rows, rounded down to whole value
    int remainder = mat->nrows % n_threads; //extra rows after dividing by number of threads
    int curr_row = 0; 
    int overall_sum = 0;

    for(int i = 0; i < n_threads; i++){ //n threads are created
        thread_data[i].mat = mat;
        thread_data[i].start = curr_row;
        curr_row = curr_row + rows;
        if (i < remainder){ // adds the remaining rows
            curr_row += 1; 
        }
        thread_data[i].end = curr_row;
        pthread_create(&threads[i], NULL, sum_result, &thread_data[i]);
    }
    for(int i = 0; i < n_threads; i++){ // joins the threads and adds each partial sum 
        int *partial_result;
        pthread_join(threads[i], (void **)&partial_result);
        overall_sum += *partial_result;
        free(partial_result); 
    }
    *result = overall_sum; // result is updated to the overall sum of the threads
    return 0;
}

int matrix_parallel_max(const matrix_t *mat, unsigned n_threads, long *result) {
    pthread_t threads[n_threads];
    thread_arguments thread_data[n_threads]; //neccessary data for each thread to operate
    int rows = floor(mat->nrows / (double)n_threads); //each thread processes this many rows, rounded down to whole value
    int remainder = mat->nrows % n_threads; //extra rows after dividing by number of threads
    int curr_row = 0;
    int overall_max = 0;

    for(int i = 0; i < n_threads; i++){ //n threads are created
        thread_data[i].mat = mat;
        thread_data[i].start = curr_row;
        curr_row = curr_row + rows;
        if (i < remainder){ // adds the remaining rows
            curr_row += 1; 
        }
        thread_data[i].end = curr_row;
        pthread_create(&threads[i], NULL, max_result, &thread_data[i]);
    }
    for(int i = 0; i < n_threads; i++){ // joins the threads and finds the overall max value
        int *partial_result;
        pthread_join(threads[i], (void **)&partial_result);
        if (*partial_result > overall_max){
            overall_max = *partial_result;
        }
        free(partial_result);
    }
    *result = overall_max; // updates the result to the overall max value of the threads
    return 0;
}

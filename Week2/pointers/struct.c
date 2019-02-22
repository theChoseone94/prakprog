#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
struct person {int age; char name[];};
typedef struct person person ;
typedef double real;
typedef struct {double re,im;} komplex;

typedef struct {int size; double data[]} vector;

vector* vector_alloc(int n){
	vector* v=malloc(sizeof(vector));
	double* a=malloc(n*sizeof(double));
	(*v).data=a;
	v->size=n;
	return v;
}

void vector_free(vector* v){
	free(v->data);
	free(v);
}

void vector_set(vector*v, int i, double value){
	assert(i>=0);
	assert(i<v->size);
	v->data[i]=value;
}

double vector_get(vector*v, int i){
	assert(i>=0);
	assert(i<v->size);
	return v->data[i];
}

int main(){
	
	vector*v;
	int n = 5;
	v=vector_alloc(n);
	for(int i=0; i<n;i++)vector_set(v,i,i);
	for(int i=0; i<n;i++)printf("v[%i]=%g\n",i,vector_get(v,i));

return 0;
}

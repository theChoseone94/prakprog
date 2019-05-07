#include<stdio.h>
#include"nvector.h"
#include<stdlib.h>
#include<assert.h>

nvector* nvector_alloc(int n){
  nvector* v = malloc(sizeof(nvector));
  (*v).size = n;
  (*v).data = malloc(n*sizeof(double));
  if( v==NULL ) fprintf(stderr,"error in nvector_alloc\n");
  return v;
}

void nvector_free(nvector* v){ free(v->data); free(v);} /* v->data is identical to (*v).data */

void nvector_set(nvector* v, int i, double value){ (*v).data[i]=value; }

double nvector_get(nvector* v, int i){return (*v).data[i]; }

double nvector_dot_product(nvector* v,nvector* u){
	assert(v->size == u->size);
	double w=0;
	for(int i=0;i<v->size;i++){
	w+= nvector_get(v,i) *nvector_get(u,i);
	};
	return w;
}







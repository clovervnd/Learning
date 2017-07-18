#include <stdio.h>
#include <string.h>
#include <malloc.h>

void main(){
	int i, *mall, *call;
	mall = (int *) malloc(3*sizeof(int));
	call = (int *) calloc(3,sizeof(int));
	printf("malloc 사용시 : ");
	for (i=0;i<3;i++){
		printf("%d ", mall[i]);
	}
	printf("\ncalloc 사용시 : ");
	for (i=0;i<3;i++){
		printf("%d ", call[i]);
	}
	putchar('\n');
}

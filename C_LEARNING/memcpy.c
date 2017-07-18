#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <malloc.h>

int main(int argv, char* argc[]){
	int a[6] = {3,4,1,6,2,5};
	int *b;
	int i;
	printf("Original message was: ");
	for (i = 0; i<6;i++){
		printf("a[%d] = %d, ",i, a[i]);
	}
	memcpy (&a[3], &a[0], sizeof(int)*3);
	
	printf("\n");
	
	printf("After memcpy: ");
	for (i = 0; i<6;i++){
		printf("a[%d] = %d, ",i, a[i]);
	}
	
	printf("\n");
	
	printf("malloc and memcpy: ");
	b = (int*)malloc(sizeof(int)*6);
	memcpy(b,a,sizeof(int)*6);
	for (i=0;i<6;i++){
		printf("b[%d] = %d, ",i, *(b+i));
	}
	printf("\n");
	printf("After changing original a[6] to 0: ");

	memset(a,0,sizeof(int)*6);
	for (i = 0; i<6;i++){
		printf("a[%d] = %d, ",i, a[i]);
	}


	printf("\n");
	for (i=0;i<6;i++){
		printf("b[%d] = %d, ",i, *(b+i));
	}
	printf("\n");
	free(b);


	return 0;
}

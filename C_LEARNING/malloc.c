#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int main(int argv, char *arg[]){
	unsigned char * pdata = 0;
	int size;

	if (argv >= 2)
		size = atoi(arg[1]);
	else {
		printf("Type the size of memory allocation :");
		scanf("%d", &size);
	}
	pdata = (char *) malloc(size);
	if (pdata == NULL){
		printf("Failed dynamic memory allocation\n");
		return -1;
	}	else
		printf("Success\n");
	
	free (pdata);
	return 0;
}

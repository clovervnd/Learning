#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argv, char * argc){
	char *ptr;

	ptr = (char*)malloc(10);

	ptr[9] = '\0';

	printf("%s\n",(char*)memset(ptr,'f',9));

	printf("%s\n",ptr);

	free(ptr);
	return 0;

}

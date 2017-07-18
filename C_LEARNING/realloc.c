#include <stdio.h>
#include <string.h>
#include <malloc.h>

void main(){

	int i, n, m;
	int *arr;
	printf("몇개의 숫자 데이터를 입력하실건가요? : ");
	scanf("%d", &n);
	arr = (int*)malloc(n*sizeof(int));
	for (i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}

	printf("입력된 데이터는");
	
	for (i =0;i<n;i++){
		printf("%d",arr[i]);
	}
	printf("입니다.\n");
	printf("추가로 몇개의 숫자 데이터를 입력하실건가요? : ");
	scanf("%d", &m);
	arr = (int *)realloc(arr, (m+n)*sizeof(int));

	for (i;i<n+m;i++){
		scanf("%d",&arr[i]);
	}

	printf("입력된 데이터는 ");
	for (i=0;i<n+m;i++){
		printf("%d", arr[i]);
	}
	printf("입니다");

	free (arr);
}

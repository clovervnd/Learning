#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

const int var = 50000000;
const int END_TIME = 100000;

void data_gen(const char * protocol, float btl_bw, char * ralg, int num_flows);

int
main(int argc, char** argv)
{
	char* protocol = "XCP";
	float btl_bw = 2.;
	char* router_alg = "RED";
	int seed = 1;
	int num_flows=1;
	int c;
	// 파라미터를 추가로 필요로하는 옵션의 경우 옵션 스트링 뒤에 ':'를 붙여준다.
	while ((c = getopt (argc, argv, "s:p:b:r:hn:")) != -1) 
	{
		switch(c)
		{
			case 's':
				// 옵션 뒤의 옵션 스트링은 optarg에 저장된다.
				seed = atoi(optarg);
				break;
			case 'p':
				protocol = optarg;
				break;
			case 'b':
				btl_bw = atof(optarg);
				break;
			case 'r':
				router_alg = optarg;
				break;
			case 'n':
				num_flows = atoi(optarg);
				break;
			case 'h':
				printf("Usage: %s -s seednum -p [XCP|YCP|ZCP] -b bottleneck_bw [2|1.5|1] -r Router_algorithm [RED|BLUE] -n num_flows\n",argv[0]);
				exit(1);
				break;
			default:
				abort();
		}
	}

	srand(seed);
	data_gen(protocol, btl_bw, router_alg, num_flows);

	return 0;
}

unsigned int rand_interval(unsigned int min, unsigned int max)
{
	int r;
	const unsigned int range = 1+max-min;
	const unsigned int buckets = RAND_MAX/range;
	const unsigned int limit = buckets * range;

	do
	{
		r = rand();
	} while (r>= limit);

	return min + (r / buckets);
}

void data_gen (const char *protocol, float btl_bw, char * ralg, int num_flows)
{
	int xcp_mean;
	int ycp_mean;
	int zcp_mean;

	float ralg_ratio = 1.;

	int mean = 0;

	if (!strcmp(ralg, "BLUE"))
	{
		ralg_ratio = 0.9;
	}
	if(!strcmp(protocol,"XCP"))
  {
  	xcp_mean = btl_bw*1000000000.*0.9*ralg_ratio/num_flows; //40%
    mean = xcp_mean;
  }
  else if (!strcmp(protocol,"YCP"))
  {
   	ycp_mean = btl_bw*1000000000.*0.6*ralg_ratio/num_flows; //30%
		mean = ycp_mean;
	}
	else if(!strcmp(protocol,"ZCP"))
	{
		zcp_mean = btl_bw*1000000000.*0.4*ralg_ratio/num_flows; //15%
		mean = zcp_mean;
	}
	else {
		fprintf(stderr,"no such protocol\n");
		exit(1);
	}
	int time; 
	for(time=0; time <= END_TIME ; time+=100)
	{
		unsigned int min_val = (unsigned int) (mean - var);
		unsigned int max_val = (unsigned int) (mean + var);
											 
		printf("%d\t",time); 
		int i;
		for(i=1; i <= num_flows; i++)
		{
			unsigned int gen_num = rand_interval(min_val, max_val);
			printf("%d\t",gen_num); 
		}
		printf("\n"); 
	}
}

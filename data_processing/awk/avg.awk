BEGIN {
	firstsim = 0;
	secondsum = 0;
}
{
	first = $1; 
	second = $2;
	firstsum += first;
	secondsum += second;
}
END {
	printf "%d\t%f, %d\t%f\n", firstsum, firstsum / NR, secondsum, secondsum/NR;
}

#include"stdio.h"
#include"string.h"

char globalvar=0;

unsigned char flag[]="REDACTED";

unsigned char op1(unsigned char a)
{
	return a^0x007;
}

unsigned char inc(unsigned char a)
{
	flag[globalvar]=a;
	globalvar++;
	return flag[globalvar];
}

unsigned char op2(unsigned char a)
{
	return (a >> 1) | (a << (8-1) );
}


int main()
{
	
	inc(op2(inc(op1(op1(inc(op2(op2(op2(inc(op1(op2(op1(inc(op2(op2(inc(op1(op2(op2(inc(op1(inc(op2(op2(op2(inc(op1(op1(op1(inc(op2(inc(op1(inc(op2(op2(op2(inc(op1(op1(op1(op2(inc(op2(op2(op2(inc(op1(op2(op2(inc(op1(op1(op1(inc(op2(op2(op2(op1(inc(op1(op2(op1(op2(inc(op1(op2(op1(inc(op2(inc(op2(inc(op1(inc(op1(inc(op2(op1(inc(op2(inc(op1(inc(op2(op1(flag[globalvar])))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))));
	for(int i=0;i<27;i++)printf("%x ",flag[i]);
	printf("\n");
	return 0;
}
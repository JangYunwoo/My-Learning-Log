/* Ex03_08.c : short형과 unsigned short형의 오버플로우 확인 2 */
#include <stdio.h>
#include <limits.h>

int main(void)
{
    short num1 = SHRT_MAX;
    short num2 = SHRT_MIN;
    unsigned short num3 = USHRT_MAX;
    unsigned short num4 = 0;

    num1 = num1 + 1;
    num2 = num2 - 1;
    num3 = num3 + 1;
    num4 = num4 - 1;

    printf("num1 = %d\n", num1);
    printf("num2 = %d\n", num2);
    printf("num3 = %d\n", num3);
    printf("num4 = %d\n", num4);

    return 0;
}
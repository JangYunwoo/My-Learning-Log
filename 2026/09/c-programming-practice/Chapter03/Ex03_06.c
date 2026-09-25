/* Ex03_06.c : signed와 unsigned 비교 */
#include <stdio.h>

int main(void)
{
    short num1 = -10;
    unsigned short num2 = num1;

    printf("부호 있는 정수 : %d\n", num1);
    printf("부호 없는 정수 : %d\n", num2);

    return 0;
}
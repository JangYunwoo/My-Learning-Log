/* Ex04_03.c : 증감 연산자 사용 예 */
#include <stdio.h>

int main(void)
{
    int count;
    int value1, value2;
    float temperature = 10.5f;

    count = 10;
    value1 = ++count;
    printf("value1 = %d, count = %d\n", value1, count);

    count = 10;
    value2 = count++;
    printf("value2 = %d, count = %d\n", value2, count);

    count = 10;
    ++count;
    printf("count = %d\n", count);

    count = 10;
    count++;
    printf("count = %d\n", count);

    temperature++;
    printf("temperature = %f\n", temperature);

    return 0;
}
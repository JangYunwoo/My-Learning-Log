/* Ex03_04.c : const 변수의 선언 및 사용 */
#include <stdio.h>

int main(void)
{
    const double PI = 3.14;
    const int MAX_COUNT;

    printf("PI = %f\n", PI);
    printf("MAX_COUNT = %d\n", MAX_COUNT);

    // PI = 3.1415; const 변수는 변경 불가
    // MAX_COUNT = 100; const 변수는 변경 불가

    return 0;
}
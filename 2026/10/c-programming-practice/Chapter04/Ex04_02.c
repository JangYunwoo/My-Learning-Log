/* Ex04_02.C : 나머지 연산자의 사용 예 */
#include <stdio.h>

int main(void)
{
    int num;
    int thousands, tens;

    printf("6자리 정수를 입력하세요 : ");
    scanf("%d", &num);

    thousands = num / 1000;
    tens = num % 1000;

    printf("%d,%d\n", thousands, tens);

    return 0;
}
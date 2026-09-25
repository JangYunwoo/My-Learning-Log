/* Ex03_01.c : 변수의 초기화 및 변수의 사용 방법 */
#include <stdio.h>

int main(void)
{
    int amount;
    int price = 1000;

    printf("수량 : %d, 가격 : %d\n", amount, price);
    
    amount = 100;
    price = 2000;
    printf("수량 : %d, 가격 : %d\n", amount, price);

    return 0;
}
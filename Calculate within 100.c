#include<stdio.h>

int main()
{
    int amount= 100;
    int price =0;

    printf("Enter the price of the item: ");
    scanf("%d", &price);

    printf("The amount before subtracting the price is: %d\n", amount);
    scanf("%d", &amount);

    int total = amount - price;

    printf("The total amount after subtracting the price is: %d\n", total);

    return 0;
}
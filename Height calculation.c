#include<stdio.h>

int main()
{
    printf("请输入身高的英尺和英寸,例如\"5 10\"表示5英尺10英寸:");

    double foot;
    double inch;

    scanf("%lf %lf", &foot, &inch);

    printf("身高为: %fm\n", (foot + inch / 12.0) * 0.3048); // 转换为米

    return 0;
}
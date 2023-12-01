#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_Digits(long number)
{
    int cont = 0;
    while (number != 0)
    {
        cont++;
        number = number / 10;
    }
    return cont;
}

int main(void)
{
    long number = get_long("Number: ");
    int s_fdigit = 0;
    int s_sdigit = 0;

    bool flag = false;

    int cant_digits = get_Digits(number);
    int card = 0;

    if (cant_digits >= 13 && cant_digits <= 16)
    {
        long coeficent = (long) pow(10, cant_digits - 2);
        card = number / coeficent;
        do
        {
            //get last two digits
            int rest = number % 100;

            int fdigit = rest % 10;
            int sdigit = (rest / 10) * 2;

            sdigit = sdigit % 10 + sdigit / 10;

            s_sdigit += sdigit;
            s_fdigit += fdigit;

            //set number
            number = number / 100;
        }
        while (number != 0);

        int total = s_fdigit + s_sdigit;
        flag = (total % 10) == 0;
    }

    if (flag)
    {
        if (card / 10 == 4)
        {
            printf("VISA\n");
        }
        else if (card == 34 || card == 37)
        {
            printf("AMEX\n");
        }
        else if (card >= 51 && card <= 55)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            flag = false;
        }
    }

    if (!flag)
    {
        printf("INVALID\n");
    }
}
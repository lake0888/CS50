#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Enter the height of the pyramid\n");
        if (height >= 1 && height <= 8)
        {
            for (int i = height; i >= 1; i--)
            {
                for (int j = 1; j <= height; j++)
                {
                    if (j < i)
                    {
                        printf(" ");
                    }
                    else
                    {
                        printf("#");
                    }
                }
                printf("\n");
            }
        }
    }
    while (height < 1 || height > 8);
}
#include <cs50.h>
#include <stdio.h>

void fromLeft(int height, int i)
{
    for (int j = 0; j < i; j++)
    {
        printf("#");
    }
}

void fromRight(int height, int i)
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
}

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Enter the height of the pyramid\n");
        if (height >= 1 && height <= 8)
        {
            int stored = height;
            for (int i = 1; i <= height; i++)
            {
                fromRight(height, stored--);
                printf("  ");
                fromLeft(height, i);
                printf("\n");
            }
        }
    }
    while (height < 1 || height > 8);
}
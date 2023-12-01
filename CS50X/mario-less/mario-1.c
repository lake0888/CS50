#include <cs50.h>
#include <stdio.h>

void fromLeftToRight(int height)
{
    for(int i = 1; i <= height; i++)
    {
        for(int j = i; j > 0; j--)
        {
            printf("#");
        }
        printf("\n");
    }
}

void fromRightToLeft(int height)
{
    for(int i = height; i >= 1; i--)
    {
        for(int j = 1; j <= height; j++)
        {
            if(j < i) printf(" ");
            else printf("#");
        }
        printf("\n");
    }
}

bool isValid(int aligntment)
{
    return (aligntment == 1 || aligntment == 2);
}

int main(void)
{
    //FROM LEFT TO RIGHT
    int height = 0;
    int aligntment = 1;
    do
    {
        height = get_int("Enter the height of the pyramid\n");
        printf("Height: %i\n", height);

        if(height >= 1 && height <= 8)
        {
            aligntment = get_int("Enter the alignment. Select 1 to alignt from Left or 2 to alignt from Right\n");
            if (isValid(aligntment))
            {
                switch(aligntment)
                {
                    case 1:
                        fromLeftToRight(height);
                        break;
                    case 2:
                        fromRightToLeft(height);
                        break;
                }
            } else printf("Choose the right option\n");
        }

    } while((height < 1 || height > 8) || (aligntment != 1 && aligntment != 2));


}
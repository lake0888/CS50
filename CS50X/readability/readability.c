#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int lenghtBy(string text, int type);
bool is_symbol(char character);
void show_result(double index);

int main(void)
{
    string text = get_string("Text: ");
    int letters = lenghtBy(text, 0);
    int words = lenghtBy(text, 1);
    int sentences = lenghtBy(text, 2);

    double L = ((double) letters / (double) words) * 100;
    double S = ((double) sentences / (double) words) * 100;

    double index = 0.0588 * L - 0.296 * S - 15.8;
    show_result(index);
}

bool is_symbol(char character)
{
    return (character == '!' || character == '.' || character == '?');
}

int lenghtBy(string text, int type)
{
    int i = 0;
    int count = 0;
    bool flag = false;
    while (i < strlen(text))
    {
        char current = toupper(text[i++]);
        switch (type)
        {
            case 0:
                flag = (current >= 'A' && current <= 'Z');
                break;
            case 1:
                flag = (current == ' ');
                break;
            default:
                flag = (is_symbol(current));
                break;
        }
        if (flag)
        {
            count++;
        }
    }
    //ADD COUNT FOR LAST CHARACTER = ' '
    if (type == 1)
    {
        count++;
    }
    return count;
}

void show_result(double index)
{
    if (index < 0)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}
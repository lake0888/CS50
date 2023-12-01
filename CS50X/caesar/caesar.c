#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char ABC[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int indexof(char letter);
int get_IndexEncrypt(int c_index, int steps);
bool only_digits(string s);

int main(int argc, string argv[])
{
    //bool main_flag = (argc == 2 && atoi(argv[1]) != 0);
    bool main_flag = (argc == 2 && only_digits(argv[1]));
    if (main_flag)
    {
        int steps = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");
        char ciphertext[strlen(plaintext)];

        int i = 0;
        while (i < strlen(plaintext))
        {
            char current = plaintext[i];
            bool flag = ((current >= 'A' && current <= 'Z') || (current >= 'a' && current <= 'z'));
            char clone = current;
            if (flag)
            {
                int c_index = indexof(current);
                int cipher_index = get_IndexEncrypt(c_index, steps);
                clone = ABC[cipher_index];
                clone = islower(current) ? tolower(clone) : clone;
            }
            ciphertext[i] = clone;
            i++;
        }

        printf("ciphertext: ");
        for (int j = 0; j < strlen(plaintext); j++)
        {
            printf("%c", ciphertext[j]);
        }
        printf("\n");
    }
    if (!main_flag)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    return 0;
}

int indexof(char letter)
{
    int index = -1;
    int i = 0;
    while (i < 27 && index == -1)
    {
        char current = ABC[i];
        if (current == toupper(letter))
        {
            index = i;
        }
        i++;
    }
    return index;
}

int get_IndexEncrypt(int c_index, int steps)
{
    return (c_index + steps) % 26;
}

bool only_digits(string s)
{
    int i = 0;
    while (i < strlen(s))
    {
        char current = s[i++];
        if (isdigit(current) == 0)
        {
            return false;
        }
    }
    return true;
}
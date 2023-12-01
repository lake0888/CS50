#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char ABC[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

bool valid(string text);
int cant(char letter, string text);
int indexof(char letter);

int main(int argc, string argv[])
{
    bool flag = true;
    if (argc == 2)
    {
        string substitution = argv[1];
        if (strlen(substitution) == 26)
        {
            if (valid(substitution))
            {
                string plaintext = get_string("plaintext: ");
                char ciphertext[strlen(plaintext)];

                int i = 0;
                while (i < strlen(plaintext))
                {
                    char current = plaintext[i];
                    int index = indexof(current);
                    ciphertext[i] = (index != -1) ? (islower(current)) ? tolower(substitution[index]) : toupper(substitution[index]) : current;
                    i++;
                }

                printf("ciphertext: ");
                for (int j = 0; j < strlen(plaintext); j++)
                {
                    printf("%c", ciphertext[j]);
                }
                printf("\n");
                flag = false;
            }
            else
            {
                flag = true;
            }
        }
        else
        {
            printf("Key must contain 26 characters\n");
            flag = false;
            return 1;
        }
    }

    if (flag)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    return 0;
}

bool valid(string text)
{
    int i = 0;
    while (i < strlen(text))
    {
        char current = toupper(text[i++]);
        if (isalpha(current) == 0 || cant(current, text) > 1)
        {
            return false;
        }
    }
    return true;
}

int cant(char letter, string text)
{
    int value = 0;
    int i = 0;
    while (i < strlen(text))
    {
        char current = toupper(text[i++]);
        if (current == toupper(letter))
        {
            value++;
        }
    }
    return value;
}

int indexof(char letter)
{
    int index = -1;
    int i = 0;
    while (i < 26 && index == -1)
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
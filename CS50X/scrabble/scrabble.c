#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
char ABC[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

int compute_score(string word);
int indexof(char letter);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // TODO: Compute and return score for string
    int score = 0;
    int i = 0;
    while (i < strlen(word))
    {
        int point = 0;
        char current = toupper(word[i]);
        if (current >= 'A' && current <= 'Z')
        {
            int index = indexof(current);
            if (index != -1)
            {
                point = POINTS[index];
            }
        }
        score += point;
        i++;
    }
    return score;
}

int indexof(char letter)
{
    int index = -1;
    int i = 0;
    while (i < 27)
    {
        char current = ABC[i];
        if (current == letter)
        {
            index = i;
        }
        i++;
    }
    return index;
}

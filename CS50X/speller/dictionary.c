// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Size of dictionary
unsigned int z_dictionary = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int i = 0;
    while (i < N)
    {
        node *cursor = table[i++];
        while (cursor != NULL)
        {
            //IS THE SAME WORD
            if (strcasecmp(cursor->word, word) == 0)
            {
                return true;
            }
            else
            {
                cursor = cursor->next;
            }
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        return false;
    }

    // We'll store the contents onto a buffer
    char *word = malloc(LENGTH + 1);

    while (fscanf(file, "%s", word) != EOF)
    {
        node *n_node = malloc(sizeof(node));

        if (n_node == NULL)
        {
            return false;
        }

        //COUNTING WORDS
        z_dictionary++;

        strcpy(n_node->word, word);
        n_node->next = NULL;

        int index = hash(n_node->word);
        if (table[index] != NULL)
        {
            node *head = table[index];
            n_node->next = head;
        }

        //UPDATE HASH TABLE
        table[index] = n_node;
    }

    free(word);
    // Close file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return z_dictionary;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int i = 0;
    while (i < N)
    {
        node *cursor = table[i++];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}

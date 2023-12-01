#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Use ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // We'll store the contents onto a buffer
    BYTE buffer[BLOCK_SIZE];
    // Number of characters read
    int num_read;

    size_t total_read = 0;

    int i_jpeg = 0;

    char *filename = malloc(1);
    FILE *img;

    int is_first = 1;

    while ((num_read = fread(buffer, 1, BLOCK_SIZE, file)) == BLOCK_SIZE)
    {
        //IS THIS A JPEG HEADER?
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (is_first == 1)
            {
                sprintf(filename, "%03i.jpg", i_jpeg);
                img = fopen(filename, "w");
                fwrite(buffer, 1, BLOCK_SIZE, img);
                i_jpeg++;
                is_first = 0;
            }
            else
            {
                fclose(img);

                sprintf(filename, "%03i.jpg", i_jpeg);
                img = fopen(filename, "w");
                fwrite(buffer, 1, BLOCK_SIZE, img);
                i_jpeg++;
            }
        }
        else
        {
            if (is_first == 0)
            {
                fwrite(buffer, 1, BLOCK_SIZE, img);
            }
        }
    }

    fclose(img);
    fclose(file);
    return 0;
}
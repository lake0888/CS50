#include "helpers.h"
#include <math.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            BYTE rgbtBlue = image[i][j].rgbtBlue;
            BYTE rgbtGreen = image[i][j].rgbtGreen;
            BYTE rgbtRed = image[i][j].rgbtRed;

            //GET AVERAGE
            int average = (int) round((double)(rgbtBlue + rgbtGreen + rgbtRed) / 3);

            //SET VALUES
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
            j++;
        }
        i++;
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width / 2)
        {

            RGBTRIPLE current = image[i][j];
            RGBTRIPLE to_replace = image[i][width - 1 - j];

            //REPLACE
            image[i][j] = to_replace;
            image[i][width - 1 - j] = current;

            j++;
        }
        i++;
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    memcpy(copy, image, sizeof(copy));

    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            //CENTER CURRENT
            int rgbtBlue = copy[i][j].rgbtBlue;
            int rgbtGreen = copy[i][j].rgbtGreen;
            int rgbtRed = copy[i][j].rgbtRed;

            int cont = 1;

            //TOP LEFT
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                rgbtBlue += copy[i - 1][j - 1].rgbtBlue;
                rgbtGreen += copy[i - 1][j - 1].rgbtGreen;
                rgbtRed += copy[i - 1][j - 1].rgbtRed;

                cont++;
            }

            //TOP CENTER
            if (i - 1 >= 0 && j >= 0)
            {
                rgbtBlue += copy[i - 1][j].rgbtBlue;
                rgbtGreen += copy[i - 1][j].rgbtGreen;
                rgbtRed += copy[i - 1][j].rgbtRed;

                cont++;
            }

            //TOP RIGHT
            if (i - 1 >= 0 && j + 1 < width)
            {
                rgbtBlue += copy[i - 1][j + 1].rgbtBlue;
                rgbtGreen += copy[i - 1][j + 1].rgbtGreen;
                rgbtRed += copy[i - 1][j + 1].rgbtRed;

                cont++;
            }

            //CENTER LEFT
            if (i >= 0 && j - 1 >= 0)
            {
                rgbtBlue += copy[i][j - 1].rgbtBlue;
                rgbtGreen += copy[i][j - 1].rgbtGreen;
                rgbtRed += copy[i][j - 1].rgbtRed;

                cont++;
            }

            //CENTER RIGHT
            if (i >= 0 && j + 1 < width)
            {
                rgbtBlue += copy[i][j + 1].rgbtBlue;
                rgbtGreen += copy[i][j + 1].rgbtGreen;
                rgbtRed += copy[i][j + 1].rgbtRed;

                cont++;
            }

            //BOTTOM LEFT
            if (i + 1 < height && j - 1 >= 0)
            {
                rgbtBlue += copy[i + 1][j - 1].rgbtBlue;
                rgbtGreen += copy[i + 1][j - 1].rgbtGreen;
                rgbtRed += copy[i + 1][j - 1].rgbtRed;

                cont++;
            }

            //BOTTOM CENTER
            if (i + 1 < height && j >= 0)
            {
                rgbtBlue += copy[i + 1][j].rgbtBlue;
                rgbtGreen += copy[i + 1][j].rgbtGreen;
                rgbtRed += copy[i + 1][j].rgbtRed;

                cont++;
            }

            //BOTTOM RIGHT
            if (i + 1 < height && j + 1 < width)
            {
                rgbtBlue += copy[i + 1][j + 1].rgbtBlue;
                rgbtGreen += copy[i + 1][j + 1].rgbtGreen;
                rgbtRed += copy[i + 1][j + 1].rgbtRed;

                cont++;
            }

            //SET VALUE WITH AVERAGE
            rgbtBlue = (int) round((double) rgbtBlue / (double) cont);
            rgbtGreen = (int) round((double) rgbtGreen / (double) cont);
            rgbtRed = (int) round((double) rgbtRed / (double) cont);

            image[i][j].rgbtBlue = rgbtBlue;
            image[i][j].rgbtGreen = rgbtGreen;
            image[i][j].rgbtRed = rgbtRed;

            j++;
        }
        i++;
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    memcpy(copy, image, sizeof(copy));

    int i = 0;
    while (i < height)
    {
        int j = 0;
        while (j < width)
        {
            int gxBlue = 0;
            int gyBlue = 0;

            int gxGreen = 0;
            int gyGreen = 0;

            int gxRed = 0;
            int gyRed = 0;

            //TOP LEFT
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                gxBlue += -1 * copy[i - 1][j - 1].rgbtBlue;
                gyBlue += -1 * copy[i - 1][j - 1].rgbtBlue;

                gxGreen += -1 * copy[i - 1][j - 1].rgbtGreen;
                gyGreen += -1 * copy[i - 1][j - 1].rgbtGreen;

                gxRed += -1 * copy[i - 1][j - 1].rgbtRed;
                gyRed += -1 * copy[i - 1][j - 1].rgbtRed;
            }
            else
            {
                gxBlue += -1 * 0;
                gyBlue += -1 * 0;

                gxGreen += -1 * 0;
                gyGreen += -1 * 0;

                gxRed += -1 * 0;
                gyRed += -1 * 0;
            }

            //TOP CENTER
            if (i - 1 >= 0 && j >= 0)
            {
                gxBlue += 0 * copy[i - 1][j].rgbtBlue;
                gyBlue += -2 * copy[i - 1][j].rgbtBlue;

                gxGreen += 0 * copy[i - 1][j].rgbtGreen;
                gyGreen += -2 * copy[i - 1][j].rgbtGreen;

                gxRed += 0 * copy[i - 1][j].rgbtRed;
                gyRed += -2 * copy[i - 1][j].rgbtRed;
            }
            else
            {
                gxBlue += 0 * 0;
                gyBlue += -2 * 0;

                gxGreen += 0 * 0;
                gyGreen += -2 * 0;

                gxRed += 0 * 0;
                gyRed += -2 * 0;
            }

            //TOP RIGHT
            if (i - 1 >= 0 && j + 1 < width)
            {
                gxBlue += 1 * copy[i - 1][j + 1].rgbtBlue;
                gyBlue += -1 * copy[i - 1][j + 1].rgbtBlue;

                gxGreen += 1 * copy[i - 1][j + 1].rgbtGreen;
                gyGreen += -1 * copy[i - 1][j + 1].rgbtGreen;

                gxRed += 1 * copy[i - 1][j + 1].rgbtRed;
                gyRed += -1 * copy[i - 1][j + 1].rgbtRed;
            }
            else
            {
                gxBlue += 1 * 0;
                gyBlue += -1 * 0;

                gxGreen += 1 * 0;
                gyGreen += -1 * 0;

                gxRed += 1 * 0;
                gyRed += -1 * 0;
            }

            //CENTER LEFT
            if (i >= 0 && j - 1 >= 0)
            {
                gxBlue += -2 * copy[i][j - 1].rgbtBlue;
                gyBlue += 0 * copy[i][j - 1].rgbtBlue;

                gxGreen += -2 * copy[i][j - 1].rgbtGreen;
                gyGreen += 0 * copy[i][j - 1].rgbtGreen;

                gxRed += -2 * copy[i][j - 1].rgbtRed;
                gyRed += 0 * copy[i][j - 1].rgbtRed;
            }
            else
            {
                gxBlue += -2 * 0;
                gyBlue += 0 * 0;

                gxGreen += -2 * 0;
                gyGreen += 0 * 0;

                gxRed += -2 * 0;
                gyRed += 0 * 0;
            }

            //CENTER
            if (i >= 0 && j >= 0)
            {
                gxBlue += 0 * copy[i][j].rgbtBlue;
                gyBlue += 0 * copy[i][j].rgbtBlue;

                gxGreen += 0 * copy[i][j].rgbtGreen;
                gyGreen += 0 * copy[i][j].rgbtGreen;

                gxRed += 0 * copy[i][j].rgbtRed;
                gyRed += 0 * copy[i][j].rgbtRed;
            }
            else
            {
                gxBlue += 0 * 0;
                gyBlue += 0 * 0;

                gxGreen += 0 * 0;
                gyGreen += 0 * 0;

                gxRed += 0 * 0;
                gyRed += 0 * 0;
            }

            //CENTER RIGHT
            if (i >= 0 && j + 1 < width)
            {
                gxBlue += 2 * copy[i][j + 1].rgbtBlue;
                gyBlue += 0 * copy[i][j + 1].rgbtBlue;

                gxGreen += 2 * copy[i][j + 1].rgbtGreen;
                gyGreen += 0 * copy[i][j + 1].rgbtGreen;

                gxRed += 2 * copy[i][j + 1].rgbtRed;
                gyRed += 0 * copy[i][j + 1].rgbtRed;
            }
            else
            {
                gxBlue += 2 * 0;
                gyBlue += 0 * 0;

                gxGreen += 2 * 0;
                gyGreen += 0 * 0;

                gxRed += 2 * 0;
                gyRed += 0 * 0;
            }

            //BOTTOM LEFT
            if (i + 1 < height && j - 1 >= 0)
            {
                gxBlue += -1 * copy[i + 1][j - 1].rgbtBlue;
                gyBlue += 1 * copy[i + 1][j - 1].rgbtBlue;

                gxGreen += -1 * copy[i + 1][j - 1].rgbtGreen;
                gyGreen += 1 * copy[i + 1][j - 1].rgbtGreen;

                gxRed += -1 * copy[i + 1][j - 1].rgbtRed;
                gyRed += 1 * copy[i + 1][j - 1].rgbtRed;
            }
            else
            {
                gxBlue += -1 * 0;
                gyBlue += 1 * 0;

                gxGreen += -1 * 0;
                gyGreen += 1 * 0;

                gxRed += -1 * 0;
                gyRed += 1 * 0;
            }

            //BOTTOM CENTER
            if (i + 1 < height && j >= 0)
            {
                gxBlue += 0 * copy[i + 1][j].rgbtBlue;
                gyBlue += 2 * copy[i + 1][j].rgbtBlue;

                gxGreen += 0 * copy[i + 1][j].rgbtGreen;
                gyGreen += 2 * copy[i + 1][j].rgbtGreen;

                gxRed += 0 * copy[i + 1][j].rgbtRed;
                gyRed += 2 * copy[i + 1][j].rgbtRed;
            }
            else
            {
                gxBlue += 0 * 0;
                gyBlue += 2 * 0;

                gxGreen += 0 * 0;
                gyGreen += 2 * 0;

                gxRed += 0 * 0;
                gyRed += 2 * 0;
            }

            //BOTTOM RIGHT
            if (i + 1 < height && j + 1 < width)
            {
                gxBlue += 1 * copy[i + 1][j + 1].rgbtBlue;
                gyBlue += 1 * copy[i + 1][j + 1].rgbtBlue;

                gxGreen += 1 * copy[i + 1][j + 1].rgbtGreen;
                gyGreen += 1 * copy[i + 1][j + 1].rgbtGreen;

                gxRed += 1 * copy[i + 1][j + 1].rgbtRed;
                gyRed += 1 * copy[i + 1][j + 1].rgbtRed;
            }
            else
            {
                gxBlue += 1 * 0;
                gyBlue += 1 * 0;

                gxGreen += 1 * 0;
                gyGreen += 1 * 0;

                gxRed += 1 * 0;
                gyRed += 1 * 0;
            }

            //SET VALUE WITH AVERAGE
            int blue = (int) round((double) sqrt((double) pow(gxBlue, 2) + (double) pow(gyBlue, 2)));
            int green = (int) round((double) sqrt((double) pow(gxGreen, 2) + (double) pow(gyGreen, 2)));
            int red = (int) round((double) sqrt((double) pow(gxRed, 2) + (double) pow(gyRed, 2)));

            if (blue > 255)
            {
                blue = 255;
            }

            if (green > 255)
            {
                green = 255;
            }

            if (red > 255)
            {
                red = 255;
            }

            image[i][j].rgbtBlue = blue;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtRed = red;

            j++;
        }
        i++;
    }
    return;
}

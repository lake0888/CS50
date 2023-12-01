#include "helpers.h"
#include <math.h>
#include <stdio.h>
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

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
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

            //SET VALUES
            int blue = (int) round(.272 * rgbtRed + .534 * rgbtGreen + .131 * rgbtBlue);
            if (blue > 255)
            {
                blue = 255;
            }
            image[i][j].rgbtBlue = blue;

            int green = (int) round(.349 * rgbtRed + .686 * rgbtGreen + .168 * rgbtBlue);
            if (green > 255)
            {
                green = 255;
            }
            image[i][j].rgbtGreen = green;

            int red = (int) round(.393 * rgbtRed + .769 * rgbtGreen + .189 * rgbtBlue);
            if (red > 255)
            {
                red = 255;
            }
            image[i][j].rgbtRed = red;

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
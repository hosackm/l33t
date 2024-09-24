#include <criterion/criterion.h>
#define STB_DS_IMPLEMENTATION
#include <stb_ds.h>

/*
 * The API provided by leetcode is garbage. So I'm changing it...
 *
 * @image - an array of arrays of shape int[cols][rows]
 * @rows  - number of rows in image
 * @cols  - number of cols in image
 * @sr    - starting row
 * @sc    - starting column
 * @color - color to swap to
 *
 * The image should be manipulated in place. No dynamic allocation is necessary.
 */
void floodFill(int **image, int rows, int cols, int sr, int sc, int color)
{
  int col = sc;
  int row = sr;
  int detected_color = image[col][row];

  if (color == detected_color)
  {
    return;
  }

  int *queue = NULL;
  arrput(queue, row);
  arrput(queue, col);

  while (arrlen(queue) > 0)
  {
    int this_row = arrpop(queue);
    int this_col = arrpop(queue);
    if (this_row < 0 || this_row >= rows || this_col < 0 || this_col >= cols)
    {
      continue;
    }

    if (image[this_row][this_col] == detected_color)
    {
      image[this_row][this_col] = color;
      // up 1
      arrput(queue, this_row - 1);
      arrput(queue, this_col);
      // down 1
      arrput(queue, this_row + 1);
      arrput(queue, this_col);
      // right 1
      arrput(queue, this_row);
      arrput(queue, this_col + 1);
      // left 1
      arrput(queue, this_row);
      arrput(queue, this_col - 1);
    }
  }
}

/*
 * Allocates a new image of size rows * columns and sets
 * the pixel values to the values in nums array.
 */
int **init_new_image(int *nums, int rows, int cols)
{
  int **image = malloc(sizeof(int *) * rows);
  for (int i = 0; i < rows; i++)
  {
    image[i] = malloc(sizeof(int) * cols);
  }

  for (int i = 0; i < rows * cols; i++)
  {
    image[i / cols][i % cols] = nums[i];
  }

  return image;
}

/*
 * Frees an image with amount of rows equal to rows.
 */
void delete_image(int **img, int rows)
{
  for (int i = 0; i < rows; i++)
  {
    free(img[i]);
  }
  free(img);
}

Test(FloodFill, FloodFillTest)
{
  {
    int inputs[9] = {1, 1, 1, 1, 1, 0, 1, 0, 1};
    int want[9] = {2, 2, 2, 2, 2, 0, 2, 0, 1};
    int rows = 3;
    int cols = 3;

    int **image = init_new_image(inputs, rows, cols);
    floodFill(image, 3, 3, 1, 1, 2);
    for (int i = 0; i < rows * cols; i++)
    {
      cr_expect(image[i / cols][i % cols] == want[i]);
    }

    delete_image(image, rows);
  }

  {
    int inputs[6] = {0, 0, 0, 0, 0, 0};
    int want[6] = {0, 0, 0, 0, 0, 0};
    int rows = 2;
    int cols = 3;

    int **image = init_new_image(inputs, rows, cols);
    floodFill(image, rows, cols, 0, 0, 0);
    for (int i = 0; i < rows * cols; i++)
    {
      cr_expect(image[i / cols][i % cols] == want[i]);
    }

    delete_image(image, rows);
  }
}

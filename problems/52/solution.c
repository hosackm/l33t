#include <stdio.h>
#include <string.h>
#include <limits.h>


#define END_OF_STR(ptr, str, len) ((ptr - str) > len)


int myisdigit(char ch)
{
    switch (ch)
    {
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
        return 1;
    }
    return 0;
}

int ctoi(char ch)
{
    switch (ch)
    {
    case '0':
        return 0;
    case '1':
        return 1;
    case '2':
        return 2;
    case '3':
        return 3;
    case '4':
        return 4;
    case '5':
        return 5;
    case '6':
        return 6;
    case '7':
        return 7;
    case '8':
        return 8;
    case '9':
        return 9;
    }
    return 0;
}


int myatoi(const char* str)
{
    const char *ptr = NULL;
    unsigned int len = 0;

    int is_negative = 0;
    int num = 0;

    if(!str)
    {
        return 0;
    }

    len = strlen(str);
    ptr = str;

    // whitespace
    while(*ptr == ' ' && !END_OF_STR(ptr, str, len))
    {
        ptr++;
    }

    if (*ptr == '-' || *ptr == '+')
    {
        is_negative = (*ptr++ == '-') ? 1 : 0;
    }

    // if it's only a sign, return 0
    if (END_OF_STR(ptr, str, len))
    {
        return 0;
    }

    // skip leading zeros
    while (*ptr == '0' && !END_OF_STR(ptr, str, len))
    {
        ptr++;
    }

    // if it was only zeros, return 0
    if(END_OF_STR(ptr, str, len))
    {
        return 0;
    }

    while (myisdigit(*ptr) && !END_OF_STR(ptr, str, len))
    {
        int digit = ctoi(*ptr);

        if (is_negative)
        {
            // detect overflow
            if (((INT_MIN + digit) / 10) > num)
            {
                return INT_MIN;
            }
            num = num * 10 - digit;
        }
        else
        {
            // detect overflow
            if (((INT_MAX - digit) / 10) < num)
            {
                return INT_MAX;
            }
            num = num * 10 + digit;
        }

        ptr++;
    }

    return num;
}

int main(int argc, char **argv)
{
    const char inputs[10] = "0123456789";
    for(int i = 0; i < 10; i++)
    {
        if(ctoi(inputs[i]) != i)
        {
            printf("TEST %d FAILED: expected %d got %d\n", i+1, i, ctoi(inputs[i]));
        }
        else
        {
            printf("TEST %d SUCEEDED\n", i+1);
        }
    }

    {
        const char input[4] = "-42";
        const int result = myatoi(input);

        if(result == -42)
        {
            printf("TEST 11 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }

    {
        const char input[3] = "42";
        const int result = myatoi(input);

        if(result == 42)
        {
            printf("TEST 12 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }

    {
        const char input[9] = "1337c0d3";
        const int result = myatoi(input);

        if(result == 1337)
        {
            printf("TEST 13 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }

    {
        const char input[4] = "0-1";
        const int result = myatoi(input);

        if(result == 0)
        {
            printf("TEST 14 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }

    {
        const char input[11] = "2147483648";
        const int result = myatoi(input);

        if(result == 2147483647)
        {
            printf("TEST 15 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }

    {
        const char input[12] = "-2147483649";
        const int result = myatoi(input);

        if(result == -2147483648)
        {
            printf("TEST 16 SUCEEDED\n");
        }
        else
        {
            printf("TEST FAILED\n");
        }
    }
}

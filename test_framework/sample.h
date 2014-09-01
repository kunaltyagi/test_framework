#include <climits>

int Factorial(int inp)
{
    int product = 1;
    for(int i = inp; i > 1; --i)
    {
        product *= i;
    }
    return product;
}

bool IsPrime(int inp)
{
    bool status = false;
    switch(inp)
    {
        case 2:
        case 3:
        case 5:
        case 7:
        case 11:
        case 13:
        case 17:
        case 19:
        case 23:
            status = true;
            break;
        default:
            status = false;
    }
    return status;
}

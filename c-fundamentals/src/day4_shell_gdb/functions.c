int add(int a, int b) { return a + b; }
int factorial(int n) { return n <= 1 ? 1 : n * factorial(n - 1);}

int main(void)
{
    add(2, 3);
    factorial(5);
    return 0;
}

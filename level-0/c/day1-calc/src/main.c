#include <stdio.h>
#include <stdlib.h>
#include "../common/calc.h"

int main(int argc, char *argv[])
{
    (void)argc;
    (void)argv;

    int a, b;
    char op;

    while (1)
    {
        printf("=== Mini Calc ===\n");
        scanf("%d %d %c", &a, &b, &op);

        switch (op)
        {
        case '+':
            printf("%d + %d = %d\n", a, b, add(a, b));
            break;
        case '-':
            printf("%d - %d = %d\n", a, b, minus(a, b));
            break;
        case '*':
            printf("%d\n", mul(a, b));
            break;
        case '/':
            if (b == 0)
            {
                fprintf(stderr, "Error: divede by zero\n");
                break;
            }
            printf("%.6f\n", divide(a, b));
            break;
        case '%':
            printf("%d\n", mod(a, b));
            break;
        default:
            fprintf(stderr, "Error: unknown op '%c'\n", op);
            break;
        }

        printf("Finish calculate.\n");

        char yes[2];
        printf("Continue? [y/n]:  ");
        fflush(stdout);

        int c;
        while ((c = getchar()) != '\n' && c != EOF);

        if (scanf("%1[yn]", yes) != 1)
        {
            break;
        }

        getchar();

        if (yes[0] == 'n')
        {
            printf("Thanks for using.\n");
            break;
        }

        else if (yes[0] == 'y')
        {
            printf("\n")
            // system("clear"); // test.sh看结果，先注释
        }
    }
    return 0;
}
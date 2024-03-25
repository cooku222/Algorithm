#include <stdio.h>

int main(){
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    int prize = 0;
    
    if (A==B && B==C){
        prize = 10000 + A*1000;
        printf("%d", prize);
    }
    else if (A==B || A==C){
        prize = 1000 + A*100;
        printf("%d", prize);
    }
    else if (B==C){
        prize = 1000 + B*100;
        printf("%d", prize);
    }
    else{
        if (A>B && A>C){
            prize = A*100;
            printf("%d", prize);
        }
        else if(B>A && B>C){
            prize = B*100;
            printf("%d", prize);
        }
        else if(C>A && C>B){
            prize = C*100;
            printf("%d", prize);
        }
    }
    return 0;
}

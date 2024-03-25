#include <stdio.h>

int main(){
    int X, N, a, b, total = 0;
    
    scanf("%d\n%d", &X, &N);
    
    for(int i=0;i<N;i++){
        scanf("%d %d", &a, &b);
        
        total += (a*b);
    }
    if(X==total){
        printf("Yes\n");
    }
    else{
        printf("No\n");
    }
    return 0;
}
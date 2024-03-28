#include <stdio.h>

int main(){
    int student[31]={0,};
    int submitNum;
    
    for(int i=0; i<28;i++){
        scanf("%d", &submitNum);
        student[submitNum]=submitNum;
    }
    
    for(int i=1; i<31;i++){
        if(student[i]==0)
            printf("%d\n", i);
    }
    return 0;
}
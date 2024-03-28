#include <stdio.h>
#include <string.h>

int main(){
    char alphabet[100];
    gets(alphabet);
    int cnt=strlen(alphabet);
    int i;
    for(i=0;i<strlen(alphabet);i++){
        if(alphabet[i]=='='){
            if(alphabet[i-1]=='c')
                cnt--;
            if(alphabet[i-1]=='s')
                cnt--;
            if(alphabet[i-1]=='z'){
                cnt--;
                if(alphabet[i-2]=='d')
                    cnt--;
            }
        }
        if(alphabet[i]=='-'){
            if(alphabet[i-1]=='c')
                cnt--;
            if(alphabet[i-1]=='d')
                cnt--;
        }
        if(alphabet[i]=='j'){
            if(alphabet[i-1]=='l')
                cnt--;
            if(alphabet[i-1]=='n')
                cnt--;
        }
    }
    printf("%d\n", cnt);
    return 0;
}
#include <stdio.h>
#include <string.h>

int main(){
    int i, j, max, result = 0, len;
    char arr[1000000];
    int cnt[26] = {0,};
    int select = 0;
    
    scanf("%s", arr);
    len = strlen(arr);
    
    for(int i='a';i<='z';i++){
        for(int j=0;j<len;j++){
            if(i==arr[j])
                cnt[i-'a']++;
        }
    }
    for(int i='A';i<='Z';i++){
        for(int j=0;j<len;j++){
            if(i==arr[j])
                cnt[i-'A']++;
        }
    }
    max=cnt[0];
    for(int i=1;i<26;i++){
        if(max<cnt[i]){
            max=cnt[i];
            select=i;
        }
    }
    
    for(int i=0;i<26;i++){
        if(max==cnt[i])
            result++;
    }
    if(result>1)
        printf("?\n");
    else
        printf("%c", select+'A');
    return 0;
}
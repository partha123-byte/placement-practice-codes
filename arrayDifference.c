#include<stdio.h>
#include<stdlib.h>

int main(){
    int n,k,arr[100],count=0;
    scanf("%d %d",&n,&k);
    for(int i = 0 ; i<n ; i++){
        scanf("%d",&arr[i]);
    }
    for(int i = 0 ; i<n ; i++){
        for(int j=i+1; j<n ;j++ ){
            if(k==abs(arr[i]-arr[j])){
                printf("%d%d\n",arr[i],arr[j]);
                count++;
            }
        }
    }

    printf("%d",count);
    return 0;
}
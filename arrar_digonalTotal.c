#include<stdio.h>

int main(){

    int n,arr[50][50],total1=0,total2=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&arr[i][j]);
        }
    }
    for(int i=0;i<n;i++){
       total1=total1+arr[i][i];
    }
   for(int i=0;i<n;i++){
       total2=total2+arr[i][n-i-1];
    }
    if((total2-total1)<0){
         printf("%d",total1-total2);
    }
    else
        printf("%d",total2-total1);
    return 0;

}
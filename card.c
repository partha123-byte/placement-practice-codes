#include<stdio.h>

int main(){
    int m,k,a,i,j,n=100;
    int arr[100][100];
    int arr1[100][100];
    int temp=0;
    scanf("%d",&m);
    scanf("%d",&k);
    a=0;
    
    for(int i=0;i<n/k;i++){
        for(int j=0;j<k; j++){
                a++;
                arr[j][i]=a;
        }
    }

    
    for(int j=0;j<k; j++){
        for(int i=0;i<n/k; i++){
                printf(" %d ",arr[j][i]);
        }
        printf("\n");
    }
    for(int j=0;j<n/k; j++){
        for(int i=0;i<k; i++){
            temp=arr[k-i-1][n/k-j-1];
           arr[j][i]=arr[k-i-1][n/k-j-1];
           arr[i][j]=temp;
        }
    }
    
    for(int j=0;j<k; j++){
        for(int i=0;i<n/k; i++){
                printf(" %d ",arr[i][j]);
        }
        printf("\n");
    }
    printf("\n%d",arr1[24,3]);
    return 0;
}
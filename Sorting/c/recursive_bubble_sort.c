#include<stdlib.h>
#include<stdio.h>
void recursive_bubble_sort(int* arr, int n){
    for(int i = 0; i < n-1; i++){
        if(arr[i+1] < arr[i]){
            int temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
            recursive_bubble_sort(arr,n);
        }
    }
}
void print_array(int* arr, int n){
    for(int i = 0; i < n; i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}
int main(){
    printf("Enter size of the array\n");
    int n;
    scanf("%d",&n);
    int* arr = (int*)malloc(sizeof(int)*n);
    printf("Enter elements of the array\n");
    for(int i = 0; i < n; i++){
        scanf("%d",(arr+i));
    }
    recursive_bubble_sort(arr,n);
    printf("After sorting the array\n");
    print_array(arr,n);
    free(arr);
    return 0;
}
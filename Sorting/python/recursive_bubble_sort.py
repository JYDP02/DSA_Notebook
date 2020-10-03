def recur_bubble_sort(arr):
    for i, ele in enumerate(arr): 
        try: 
            if arr[i+1] < ele: 
                arr[i] = arr[i+1] 
                arr[i+1] = ele 
                recur_bubble_sort(arr) 
        except IndexError: 
            pass
    return arr 
def main():
    print("Enter elements of the array separated by a space")
    arr = list(map(int,input().split()))
    recur_bubble_sort(arr)
    print("Array after sorting = ")
    print(arr)
if __name__ == '__main__':
    main()

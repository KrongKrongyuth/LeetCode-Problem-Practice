#include <stdio.h>

void print_array(int[], int);
// int check_value(int, int[]);

int main(){
    int array[3] = {1,1,2};
    removeDuplicates(array, 3);

    return 0;
}

int removeDuplicates(int* nums, int numsSize) {
    // Pointer
    int * pArray_size;

    int array_size;
    int expectedNums[array_size+1];

    array_size = sizeof(nums)/sizeof(nums[0]);
    pArray_size = &array_size;

    for (int i = 0; i <= *pArray_size; i++)
    {
        // printf("%d\t%d\n", nums[i], i);
        switch (i)
        {
            case 0 :
                expectedNums[i] = nums[i];
                break;
            default:
                // switch (nums[i])
                // {
                //     case :

                // }
                break;
        }
    }
    array_size = sizeof(expectedNums)/sizeof(expectedNums[0]);
    pArray_size = &array_size;

    print_array(expectedNums, *pArray_size);
    // check_value(1, expectedNums);

    return numsSize;
}

void print_array(int array[], int size){
    // int array_size = sizeof(array)/sizeof(array[0]);
    for (int i = 0; i <= size; i++){
        printf("%d\n", array[i]);
    }
}

int check_value(int value, int array[]){
    int array_size = sizeof(array)/sizeof(array[0]);
    for (int i = 0; i <= array_size; i++){
        if (value == array[i])
        {
            printf("%d", array[i]);
        }
        else
        {
            printf("%d", array[i]);
        }
    }
    return 1;
}
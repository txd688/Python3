'''
原理

插入排序（Insertion Sort）是一种简单直观的排序算法。
它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤

从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
'''
def insertion_sort(arr):
    arrlen = len(arr)

    for i in range(1,arrlen):
        if arr[i] < arr[i-1]:
            #后一个元素比前一个元素小
            temp = arr[i]
            index = i

            #从已排序的list进行比较
            for j in range(i-1,-1,-1):
                if(arr[j] > temp):
                    arr[j + 1] = arr[j]
                    index = j
                else:
                    break
                
            arr[index] = temp
            
    return arr;

arr = [3,44,38,34,15,5,20,30,58,23,34,19]

print(insertion_sort(arr))

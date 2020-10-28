'''
选择排序（Selection sort）是一种简单直观的排序算法。
它的工作原理大致是将后面的元素最小元素一个个取出然后按顺序放置。

步骤

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。

'''

def selection_sort(arr):
    arrlen = len(arr)
    
    for i in range(arrlen):
        small = i
        for j in range(i+1,arrlen):
            if(arr[small] > arr[j]):
                #找到最小的
                small = j
                
        arr[small], arr[i] = arr[i], arr[small]
                
    return arr;

arr = [3,44,38,34,15,5,20,30,58,23,34,19]

print(selection_sort(arr))

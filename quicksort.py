# Write your code here :-)
# print("QuickSort")
class QuickSort:
    def __init__(self,arr, left, right):
        self.arr = arr
        self.left = left
        self.right = right

    def Partition(self,arr,left,right):
        pivot = arr[left]
        while(True):
            while(arr[left] < pivot):
                left+=1
            while(arr[right] > pivot):
                right-=1
            if (left < right):
                temp = arr[right]
                arr[right] = arr[left]
                arr[left] = temp
            else:
                return right

    def quickSort(self, arr, left, right):
        if(left < right):
            pivot = self.Partition(arr,left,right)
            if(pivot > 1):
                self.quickSort(arr,left, pivot - 1)
            if(pivot + 1 < right):
                self.quickSort(arr,pivot + 1,right)
    def displayArr(self):
        for i in self.arr:
            print(i,end=' ')

def main():
    arr = [67,12,95,56,85,1,100,23,60,9]
    print("QuickSort starting")
    test = QuickSort(arr, 0, 9)
    print ("Array Loaded")
    test.displayArr()
    test.quickSort(test.arr, test.left, test.right)
    print ("")
    print ("Array Sorted")
    test.displayArr()


if __name__ == "__main__":
    main()
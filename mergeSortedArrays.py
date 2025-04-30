class Merge():
    def mergeArrays(self,arr1,arr2):

        arr=[]
        i,j=0,0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
        while i<len(arr1):
            arr.append(arr1[i])
            i+=1
        while j<len(arr2):
            arr.append(arr2[j])
            j+=1

        print(arr)


merge = Merge()
merge.mergeArrays([1,2,3,4],[2,3,4,5])

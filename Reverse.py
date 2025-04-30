class Reverse():
    def reverse(self,string):
        j=0
        arr=[]
        for i in range(len(string)-1,0,-1):
            arr.append(string[i])
            j=j+1 
        print(arr)

rev = Reverse()
rev.reverse("Hi I am Johann")

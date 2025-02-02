def has_33(nums):
    n=len(nums)
    for i in range(n-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

mylist=list(map(int, input("Numbers:").split()))
if has_33(mylist):
    print("Array contains 3 next to 3")
else:
    print("Array does not contain 3 next to 3")
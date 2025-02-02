def spy_game(nums):
    n=len(nums)
    for i in range(n-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            return True
    return False

mylist=list(map(int, input("Numbers:").split()))
if spy_game(mylist):
    print("Array contains 007")
else:
    print("Array does not contain 007")
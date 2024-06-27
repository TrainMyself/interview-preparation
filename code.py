def sort(nums):
    p0,p1,p2 = -1,-1,len(nums)
    length = len(nums)
    p=0
    while p < length:
        if p == p2:
            break
        if nums[p] == 0:
            p0+=1
            p1+=1
            nums[p0]=0
            if p0 != p1:
                nums[p1]=1
        elif nums[p] == 1:
            p1+=1
            nums[p1]=1
        else:
            p2-=1
            nums[p],nums[p2] = nums[p2],nums[p]
            continue
        p+=1
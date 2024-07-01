def merge(nums1, nums2, m, n):
    X = max(max(nums1),max(nums2))
    i,j,k = 0,0,0
    flag = True
    while j < m or k < n:
        if j == m and k < n:
            if flag:
                nums1[i] = (nums2[k]%X)*X + nums1[i]
            else:
                nums2[i] = (nums2[k]%X)*X + nums2[i]
            k+=1
            i+=1
            if i == m and flag == True:
                i=0
                flag=False
            continue
        
        if k == n and j < m:
            if flag:
                nums1[i] = (nums1[j]%X)*X + nums1[i]
            else:
                nums2[i] = (nums1[j]%X)*X + nums2[i]
            j+=1
            i+=1
            if i == m and flag == True:
                i=0
                flag=False
            continue
        
        if nums1[j]%X < nums2[k]%X:
            if flag:
                nums1[i] = (nums1[j]%X)*X + nums1[i]
            else:
                nums2[i] = (nums1[j]%X)*X + nums2[i]
            j+=1
            i+=1
        else:
            if flag:
                nums1[i] = (nums2[k]%X)*X + nums1[i]
            else:
                nums2[i] = (nums2[k]%X)*X + nums2[i]
            k+=1
            i+=1

        if i == m and flag == True:
            i=0
            flag=False
    
    for i in range(m):
        nums1[i]=nums1[i]//X
    for i in range(n):
        nums2[i]=nums2[i]//X
    
    return nums1,nums2   
        
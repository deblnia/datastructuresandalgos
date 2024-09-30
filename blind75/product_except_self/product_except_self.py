def productExceptSelf(nums): 
    ans = []
    tmp_product = 1 
    for i in range(len(nums)):
        ans.append(tmp_product)
        tmp_product *= nums[i] 
    return ans 




if __name__ == '__main__': 
    assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
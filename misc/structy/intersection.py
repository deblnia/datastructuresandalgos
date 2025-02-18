def intersection(a, b): 
    # ans = []
    # for i in a: 
    #     for j in b: 
    #         if i == j: 
    #             ans.append(i)
    #             break
    # return sorted(ans)
    # ans = []
    # for i in a:
    #     if i in j:
    #         ans.append(i)
    # return ans 
    # ans = []
    # setA = set(a)
    # for i in b: 
    #     if i in setA:
    #         ans.append(b)
    # return ans 

    ans = []
    setA = set(a)
    return sorted([item for item in b if item in setA])




assert intersection([4,2,1,6], [3,6,9,2,10]) == [2,6]
assert intersection([2,4,6], [4,2]) == [2,4]
assert intersection([4,2,1], [1,2,4,6]) == [1,2,4]
assert intersection([0,1,2], [10,11]) == []

a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
assert intersection(a, b) == [ i for i in range(0, 50000) ]
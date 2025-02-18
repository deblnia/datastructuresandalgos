def zipper_lists(head1, head2): 
    curr1 = head1.next  
    curr2 = head2
    tail = head1 

    count = 0 
    while curr1 is not None and curr2 is not None:  
        if count % 2 == 0: 
            tail.next = curr2
            curr2 = curr2.next 
        else:
            tail.next = curr1
            curr1 = curr1.next 
        tail = tail.next 
        count += 1 
    if curr1 is not None: 
        tail.next = curr1 
    if curr2 is not None: 
        tail.next = curr2 
    return head1 

    # here's the recursive way - some echos of similarity 
    # if head_1 is None and head_2 is None: 
    #     return None 
    # if head_1 is None: 
    #     return head_2 
    # if head_2 is None: 
    #     return head_1
  
    # next1 = head_1.next
    # next2 = head_2.next 
    # head_1.next = head_2
    # head_2.next = zipper_lists(next1, next2)
    # return head_1
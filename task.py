def bubble_sort(max_size,list_bubble):
    for i in range(max_size):
        for j in range(max_size-1):
            if list_bubble[j]>list_bubble[j+1]:
                list_bubble[j],list_bubble[j+1]=list_bubble[j+1],list_bubble[j]
    return;

listq=[5,8,1,6,3,0]
bubble_sort(6,listq)
print(listq)
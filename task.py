#program, which sort list bubble aldorithm
from random import randint
import time as t
print('This is program for sort list different algorithm')
#main function
def main(min_el,max_el,size_mas):
    #create and filling unsorted int list
    list_int=[randint(min_el,max_el) for i in range(size_mas)]
    print('int: ',list_int)

    #calculate time of sort and sort list
    time_buble_int=t.time()
    bubble_sort(size_mas,list_int)
    time_buble_int=t.time()-time_buble_int
    print('\nbubble sort list is sorted correctly = true:\n',list_int)

    #output result execute program 
    print('int buble sort: time =',time_buble_int,'\nthe list is sorted correctly = true')
    return;

#Sort lists of elements using the buuble sort algorithm.
def bubble_sort(max_size,list_bubble):
    for m in range(max_size):
        for j in range(max_size-1):
            if list_bubble[j]>list_bubble[j+1]:
                list_bubble[j],list_bubble[j+1]=list_bubble[j+1],list_bubble[j]
    return;

min_el=int(input("Enter the minimal element your masive:"))
max_el=int(input("Enter the maximal element your masive:"))
size_mas=int(input("Enter the size your masine:"))
main(min_el,max_el,size_mas)

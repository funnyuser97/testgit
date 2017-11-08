#program, which sort list bubble aldorithm
from random import randint
#constant
MAX_EL=99
MIN_EL=0
SIZE_MAS=100
#main function
def main():
    #create and filling unsorted int list
    list_int=[randint(MIN_EL,MAX_EL) for i in range(SIZE_MAS)]
    print('int: ',list_int)

    bubble_sort(SIZE_MAS,list_int)
    print('\nbubble sort list is sorted correctly = true:\n',list_int)  

    return;

#Sort lists of elements using the buuble sort algorithm.
def bubble_sort(max_size,list_bubble):
    for i in range(max_size):
        for j in range(max_size-1):
            if list_bubble[j]>list_bubble[j+1]:
                list_bubble[j],list_bubble[j+1]=list_bubble[j+1],list_bubble[j]
    return;

main()

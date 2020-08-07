a = [2, 4, 6, 8, 10, 12, 14, 16, 18]

def BinarySearch(list, number):
    length = len(list)
    c1 = int(length/2)
    if length==0:
        print("The number is not in the list.") 
        return False
    elif number==list[c1]:
        return c1
    elif number>list[c1]:
        return BinarySearch(list[c1+1:],number)+(c1+1)
    elif number<list[c1]:
        return BinarySearch(list[:c1],number)

index = BinarySearch(a,8)

print(index)

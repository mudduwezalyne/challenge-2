def Fizzbuzz(list1, list2):

    a = len(list1)
    b = len(list2)

    p = a+b
 
    if p%3 == 0:
        return "Fizz"

    elif p%5 == 0:
        return "Buzz"

    elif p%5 == 0 and p%3 == 0:        
        return "Fizzbuzz"
    
print(Fizzbuzz([3,6,9], [2,4,8]))

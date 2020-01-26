
import array as arr
a=arr.array('i',(1,2,3,4,6,7))
#print(type(a))
while True:
    print("1. Print Array")
    print("2. Add Elements")
    print("3. Delete Elemants")
    print("4. Exit")
    choice=int(input("Enter your Choice here: "))

    if choice == 1:
        print("The Array Elements are: ",a)
        #for i in a:
         #   print(i)
    elif choice == 2:
        print("Please enter a valid number")
        try:
            num=int(input("Enter a number: "))
        except Exception:
            print("Enter integer numbers only")
        a.append(num)

    elif choice == 3:
        x= a.pop()
        print("The deleted value is : ",x)
    elif choice == 4:
        break
    else:
        print("Please enter a valid choice")



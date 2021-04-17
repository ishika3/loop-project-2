def code1():
    list1=[12,-7,5,64,-14]
    for num in list1:
        if num>=0:
            print(num,end=',')

def code2():
    list2=[12,14,-95,3]
    for num in list2:
        if num>=0:
            print(num,end=',')\

def main():
    while True:
        selection=int(input("enter choice:"))

        if selection==1:
            code1()
        elif selection==2:
            code2()
        else:
            print("invalid text")
main()

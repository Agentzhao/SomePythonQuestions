def decimaltobinary(dec):
    num = int(dec)
    binary = []
    while (num > 0):
        rem = num % 2
        binary.append(str(rem))
        num = num // 2
    binary.reverse()
    return(''.join(binary))

range1 = input("Enter the range of numbers from n: ")
range2 = input("to m: ")

numberofboxes = len(decimaltobinary(range2))

box1 = []
box2 = []
box4 = []
box5 = []
array = []
for i in range(int(range1),int(range2)):
    array.append(decimaltobinary(i))
              


##
##box1 = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
##box2 = [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
##box3 = [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
##box4 = [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
##box5 = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
##
##print(box1)
##print(box2)
##print(box3)
##print(box4)
##print(box5)
##
##boxes = []
##numbers = input("Enter the boxes your number is in: ")
##numbers.append(boxes)

import math

# Taking the dimensions of the wall from the user.

wallLength = input("Enter wall length:")
wallHeight = input("Enter wall height:")

#function to calculate the no and type of boards requird to fit the wall with minimum wastage.

def boards_Required(length, height):
    ret_Length = length
    ret_Height = height
    board_Lengths = [1800, 2400, 2700, 3000]
    board_Height = 1200


    for x in board_Lengths:
        if int(length) <= int(x) :
            ret_Length = x
            noLength= 0
            break


    if int(length) > int(max(board_Lengths)):
       noLength = int(int(length) /int(min(board_Lengths)))
       remaining_length = int(length) - (int(noLength) * int(max(board_Lengths)))
       for x in board_Lengths:
           if remaining_length <= int(x):
               ret_Length = x
               break



    if int(height) > int(board_Height) :
        levels_num = int(int(height)/1200)
        levels_num += 1
    else:
        levels_num = 1


    finalnum = levels_num * noLength



    return(finalnum, levels_num, ret_Length, )

# calling function .
results = boards_Required(wallLength,wallHeight)

if results[0] > 0:
    print(f'you need {results[0]}, of 1800*1200 and')
    print(f'you need {results[1]}, of {results[2]}*1200')
else:
    print(f' you need {results[1]} of {results[2]}*1200')




















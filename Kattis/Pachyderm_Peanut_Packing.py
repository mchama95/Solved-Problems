"""
https://open.kattis.com/problems/pachydermpeanutpacking
Naga Manikanta Chama 
mchama95@gmail.com

"""


def point_in_rectangle(x1y1x2y2, xy):
    """
    Finds if the given point xy exists in the rectangle x1y1x2y2
    :param x1y1x2y2: box coordinates
    :param xy: point coordinates
    :return: bool
    """
    if (float(x1y1x2y2[0]) <= float(xy[0]) <= float(x1y1x2y2[2])) and (
            float(x1y1x2y2[1]) <= float(xy[1]) <= float(x1y1x2y2[3])):
        return True
    else:
        return False


while True:
    # print('Enter n: ')
    n = int(input()) # Get number of boxes
    if n == 0:
        # Beak if number of boxes is 0
        break
    else:
        box = [] # array to store box coordinates
        for _ in range(0, n):
            # print('Enter box %d description: ' % (_ + 1))
            box.append(list(input().split(' '))) # Split into x1, y1, x2, y2, size of the box

        # print('Enter m: ')
        m = int(input()) # Get number of peanuts

        for _ in range(0, m):
            # print('Enter peanut %d description: ' % (_ + 1))
            peanut = list(input().split(' ')) # Split into x, y1, size of the peanut
            boxSearchFlag = True # Exit the loop if peanut can fit in a box
            boxInd = 0
            while boxInd < n and boxSearchFlag:
                # print('{}'.format(box[boxInd]))
                if point_in_rectangle(box[boxInd], peanut):
                    # print('I am here 1')
                    if box[boxInd][-1] == peanut[-1]: # check if peanut size and box size are the same
                        # print('I am here 2')
                        print(peanut[-1] + ' correct')
                        boxSearchFlag = False
                    else:
                        # print('I am here 3')
                        print(peanut[-1] + ' ' + box[boxInd][-1])
                        boxSearchFlag = False
                elif boxInd == n - 1:
                    # print('I am here 4')
                    print(peanut[-1] + ' floor')

                boxInd = boxInd + 1

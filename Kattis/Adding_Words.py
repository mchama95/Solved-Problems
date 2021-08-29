"""
    https://open.kattis.com/problems/addingwords
    Naga Manikanta Chama
    mchama95@gmail.com

"""

import sys

data = {}  # To hold the data
data_reverse = {}

run_flag = True
for line in sys.stdin.readlines():
    # Get input
    get_input = line.split()

    # if def store value
    if get_input[0] == 'def':
        data[get_input[1]] = int(get_input[2])
        data_reverse[int(get_input[2])] = get_input[1]
    # if clear, delete the data
    elif get_input[0] == 'clear':
        data.clear()
        data_reverse.clear()
        run_flag = False
    # If calc, start calculating
    elif get_input[0] == 'calc':

        temp_val1 = []  # to hold the formatted string
        if not set(get_input[1:-1:2]) <= set(data.keys()):  # Check if the parameters are already in database
            print(' '.join(get_input[1:]),  'unknown')
        else:
            # Start calculating
            for calcInd in get_input[1:]:
                if calcInd == '=':
                    temp_val = int(eval(''.join(temp_val1)))
                    if temp_val in data.values():
                        print(' '.join(get_input[1:]), data_reverse[temp_val])
                    else:
                        print(' '.join(get_input[1:]), 'unknown')
                else:

                    if calcInd in data.keys():
                        temp_val1 += str(data[calcInd])
                    else:
                        temp_val1 += calcInd

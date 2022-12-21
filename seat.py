import json



def print_values(seats, col_size, row_size):
    string_j = ''
    for i in range(col_size):
        for j in range(row_size):
            try:
                if seats[j] is None or seats[j][i] is None:
                    string_j += "- "
                    continue
            except IndexError:
                continue

            try:
                for k in range(len(seats[j][i])):
                    string_j += f"{seats[j][i][k]} "
            except IndexError:
                continue
            string_j += ","
        string_j += "\n"
    print(string_j)


def fill_with_ma_and_w(array):
    seats = []
    for i in range(len(array)):
        seats.append([["M"] * array[i][0] for _ in range(array[i][1])])
    #print(seats)
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            seats[i][j][0] = "A"
            seats[i][j][-1] = "A"
    for i in range(len(seats[0])):
        seats[0][i][0] = "W"
    for i in range(len(seats[-1])):
        seats[-1][i][-1] = "W"
    
    return seats

def replace_with_number(val, counter, seats, col_size, row_size, cnt):
    if(counter>cnt):
        return
    print(col_size, row_size)
    for i in range(col_size):
       
        for j in range(row_size):
            try:
                if seats[j] is None or seats[j][i] is None:
                    continue
            except IndexError:
                continue
            try:
                for k in range(len(seats[j][i])):
                    if(counter>cnt):
                        return 
                    #print(j,i,k, seats[j][i][k])
                    if seats[j][i][k] == val:
                        seats[j][i][k] = counter
                        counter += 1
            except IndexError:
                continue
    return {'seats': seats, 'counter': counter}


if __name__ == "__main__":
    input_string = input('Enter the seats as arrays in json notation ')
    array = json.loads(input_string)
    
    row = max(int(e[0]) for e in array)
    col = max(int(e[1]) for e in array)
    cnt = int(input('Enter the number of passengers waiting in the queue '))
    seats = fill_with_ma_and_w(array)
    #print(seats)
    obj = {}
    
    obj = replace_with_number('A', 1, seats, col, row, cnt)
    obj = replace_with_number('W', obj['counter'], obj['seats'], col, row, cnt)
    obj = replace_with_number('M', obj['counter'], obj['seats'], col, row, cnt)
    #seats = obj['seats']
    print_values(seats, col, row)

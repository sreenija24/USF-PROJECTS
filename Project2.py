# solving the maze using stack implementation
import sys
input_file = sys.argv[1]  # taking inputs from command line arguments
output_file = sys.argv[2]
input = open(input_file)    #openeing the input_file as input
x, y = input.readline().split()     #getting the row and column from first line of input
m = int(x) #row
n = int(y)  #column
    #print(rows, cols)
graph = input.read().splitlines()
#print(graph)
input.close()
col_dir = [['' for j in range(n)] for i in range(m)] #empty 2d array to store the color_direction values
for i in range(0,m):
    each_row=graph[i].strip().split()
    #print(each_row)
    for j in range(0,len(each_row)):
        col_dir[i][j] = each_row[j]


##print(col_dir)
#assigning false to all col_dir values in graph as they are not visited at first
visited = [[False for j in range(n)] for i in range(m)]  #2d array of same size as col_dir
stack=[]    #creating an empty list(stack) to store indices of the elements that are traversed in col_dir matrix
current_element=col_dir[0][0] #initializing left most top element to the current element
count=1
stack.append([0,0]) #pushing the first element as it is visited
row=0
col=0
ele=[]
isBull=False #if bulls eye is arrived the isBull is set to True
#traverse if row and column does not go index out of bounds
while(row>=0 and row<m and col>=0 and col<n and not isBull):
    #print(current_element,end=" ")
    if(current_element=='O'):
        stack.append([row,col])
        isBull = True
        break
    if(row==0 and col==0):
        #stack.append([row,col])
        visited[row][col] = True
    color = current_element.split("-")[0]
    #if color is red then assign Blue to oppcolor and vice versa
    if(color=='R'):
        opp_color='B'
    elif(color=='B'):
        opp_color='R'
    else:
        break
    prev_row, prev_col = stack[count-1] #store previous indices
    #print("prev   ",stack[count-1])
    direction = current_element.split("-")[1]
    # loop until we find opp_color in the above direction eg:(R-S)
    temp_element = current_element
    #get the row and col of next element which could be in path,
    # if index is in range and temp_color is not opposite colr
    # or if temp_color is opp_color and it is being visited
    while((row>=0 and row<m and col>=0 and col<n) and (temp_element.split("-")[0]!=opp_color or visited[row][col]==True)):
        #print(row,col,direction)
        if(direction == 'E'):
                row=row
                col=col+1
        elif(direction == 'W'):
                row=row
                col=col-1
        elif(direction == 'S'):
                row=row+1
                col=col
        elif(direction == 'N'):
                row=row-1
                col=col
        elif(direction == 'NE'):
                row=row-1
                col=col+1
        elif(direction == 'NW'):
                row=row-1
                col=col-1
        elif(direction == 'SE'):
                row=row+1
                col=col+1
        elif(direction == 'SW'):
                row=row+1
                col=col-1
        # if it traverses to index not in range,pop the element(source_element) in stack
        if ((row < 0 or row >= m or col < 0 or col >= n)):
            # row, col = stack.pop()
            stack.pop()
            # popped.append(ele)
            count = count - 1
            row, col = stack[count - 1]     #getting the previous rows and cols from stack and assign it to current rows,cols
            current_element = col_dir[row][col]
            #print("count", count)
            break
        else:
            temp_element=col_dir[row][col]
            temp_color = temp_element.split("-")[0]
            #print("updated   ",row,col)
        if(temp_element=='O'):  #if the temp_element reaches bulls eye,break
            stack.append([row,col])
            isBull=True
            break
        #if the next element is not visited yet and is of opp_color of current color
        # then append the element into the stack
        if (temp_color == opp_color and visited[row][col] == False and row >= 0 and row < m and col >= 0 and col < n):
            current_element = col_dir[row][col]
            stack.append([row, col])
            count = count + 1
            visited[row][col] = True
            #print("appended ", [row, col])
            break

#print("stack",stack)
f = open(output_file, "w") #openeing the output file in write mode
target_path = '' #initializing the final path
for i in range(0,len(stack)):
    m=stack[i][0] #row
    n=stack[i][1] #col
    if(stack[i][0]==stack[i+1][0]):
        distance=abs(stack[i][1]-stack[i+1][1])  #distance=abs(prev_row-current_row)
    elif(stack[i][1]==stack[i+1][1]):
        distance = abs(stack[i][0] - stack[i + 1][0])  #distance=abs(prev_col-current_col)
    else:
        distance=abs(stack[i][1]-stack[i+1][1])    #distance =  difference of either rows or cols

    target_path = str(distance)+col_dir[stack[i][0]][stack[i][1]].split("-")[1]+' '  #concatinating the whole path
    #print(str(distance)+col_dir[stack[i][0]][stack[i][1]].split("-")[1],end=" ")



    #write into file
    f.write(target_path)  #writing the target_path
##print("stack",stack)














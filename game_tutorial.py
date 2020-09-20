num_rows = 10
num_cols = 10
matrix = []

def create_matrix():
	for i in range(num_rows):
		cols = []
		for j in range(num_cols):	
			cols.append('*')
		matrix.append(cols)

def print_matrix():
	for i in range(num_rows):
		for j in range(num_cols):
			print(matrix[i][j], end='')
		print()

def update_matrix(x, y):
	if(matrix[x][y] == ' '):
		print("You lose!")
	else:
		matrix[x][y] = ' '

create_matrix()
print_matrix()

up = 'w'
left = 'a'
down = 's'
right = 'd'

x = 5
y = 5

while(True):
	update_matrix(x,y)	
	print_matrix()
	inp = input()
	if(inp == up):
		x = x-1
	if(inp == down):
		x = x+1
	if(inp == left):
		y = y-1
	if(inp == right):
		y = y+1
		

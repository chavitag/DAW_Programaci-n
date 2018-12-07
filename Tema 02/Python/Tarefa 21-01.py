def fill0(board):
	for f in range(len(board)):
		for c in range(len(board[f])):
			board[f][c]=0;

def show(board):
	for f in range(len(board)):
		print
		for c in range(len(board[f])):
			print board[f][c],
	print


taboa=[ [0,0,1,0,2,0,0,1],
        [0,0,0,2,1,1,0,2],
        [0,1,1,2,0,1,0,1],
        [0,2,0,2,1,2,0,2],
        [0,1,1,0,2,0,2,0],
        [0,2,2,0,2,1,2,1],
        [2,0,0,1,0,2,2,2],
        [0,0,0,0,0,0,0,0] ];

show(taboa)
fill0(taboa)
print "------------------"
show(taboa)

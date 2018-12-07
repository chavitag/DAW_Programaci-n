def countNearOne(board):
	cta=0
	for f in range(len(board)):
		for c in range(len(board[f])):
			if (hasNearOne(board,f,c)):
				cta=cta+1
	return cta

def hasNearOne(board,f,c):
	if (board[f][c]==0):
		if (c>0) and (board[f][c-1]==1):
			return True
		if (c<7) and (board[f][c+1]==1):
			return True
		if (f>0):
			if (c>0) and (board[f-1][c-1]==1):
				return True
			if (board[f-1][c]==1):
				return True
			if (c<7) and (board[f-1][c+1]==1):
				return True
		if (f<7):
			if (c>0) and (board[f+1][c-1]==1):
				return True
			if (board[f+1][c]==1):
				return True
			if (c<7) and (board[f+1][c+1]==1):
				return True
	return False

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
print("Existen "+str(countNearOne(taboa))+" celas con polo menos un 1 ao redor")


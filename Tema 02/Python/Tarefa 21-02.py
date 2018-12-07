def diagonal(board,f,c,val,numv):
	while ((f<8) and (c<8) and (numv>0)):
		board[f][c]=val;
		f=f+1;
		c=c+1;
		numv=numv-1;

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
diagonal(taboa,2,2,9,5);
print "------------------"
show(taboa)
diagonal(taboa,0,5,9,9);
print "------------------"
show(taboa)

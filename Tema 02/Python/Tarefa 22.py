def reverse(board,f,c):
	dirs=[[1,1],[-1,-1],[1,-1],[-1,1],[0,1],[0,-1],[1,0],[-1,0]]
	cta=0
	for d in dirs:
		cta=cta+test(board,f,c,d[0],d[1])
	return cta

def test(board,f,c,df,dc):
	if (board[f][c]!=0):
		return 0
	row=f+df
	col=c+dc
	cta=0
	if (col>=0) and (col<8) and (row<8):
		while (row>=0) and (row<8) and (col>=0) and (col<8) and (board[row][col]==2):
			cta=cta+1
			row=row+df
			col=col+dc
		if (row<0) or (row>7) or (col<0) or (col>7) or (board[row][col]!=1):
			cta=0
		else:
			setToOne(board,row-df,col-dc,cta,-df,-dc)
	return cta

def setToOne(board,f,c,numc,dr,dc):
	while(numc>0):
		board[f][c]=1
		f=f+dr;
		c=c+dc
		numc=numc-1

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
print("------------------------------");
print("Test (0,2): "+str(reverse(taboa,0,2))+" celas. Taboleiro resultante: ")
show(taboa)
print("------------------------------");
print("Test (0,4): "+str(reverse(taboa,0,4))+" celas. Taboleiro resultante: ")
show(taboa)
print("------------------------------");
print("Test (0,0): "+str(reverse(taboa,0,0))+" celas. Taboleiro resultante: ")
show(taboa)
print("------------------------------");
print("Test (2,4): "+str(reverse(taboa,2,4))+" celas. Taboleiro resultante: ")
show(taboa)
print("------------------------------");
print("Test (5,3): "+str(reverse(taboa,5,3))+" celas. Taboleiro resultante: ")
show(taboa)
print("------------------------------");
print("Test (7,5): "+str(reverse(taboa,7,5))+" celas. Taboleiro resultante: ")
show(taboa)

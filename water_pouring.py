def solutions(x,y,X,Y):
	print ('X={},Y={}'.format(X,Y))
	return {
			(X,y):'fill X',
			(x,Y):'fill Y',
			((0,y+x) if y+x <=Y else (x-(Y-y),Y)):'X->Y' ,
			((x+y,0) if x+y<=X else (X,y-(X-x))):'Y->X',
			(0,y):'empty x',
			(x,0):'empty y'
			}

res=[]
def pour_problem(X,Y,goal,start=(0,0)):
	if goal in start:
		return [start]
	explored=set()
	frontier=[[start]]
	i=0
	while frontier:
		print ('frontier:',frontier )#两层列表
		path=frontier.pop(-1)#一层列表
		print ('path:',path)
		(x,y)=path[-1]
		i+=1
		for (state,action) in solutions(x,y,X,Y).items():
			print ('{}th>>:state:{},action:{}'.format(i,state,action))
			if state not in explored:
				explored.add(state)
				print ('explored:{}'.format(explored))
				path2=path+[action,state]
				# print 'path2:',path2
				if goal in state:
					# res.append(path2)
					# print '>>>>>path2:',path2
					return path2
				else:
					# print '>>path2:',path2
					frontier.append(path2)
			# print 'explored:{}'.format(explored)
	return Fail

Fail=[]
print (pour_problem(3,5,4))

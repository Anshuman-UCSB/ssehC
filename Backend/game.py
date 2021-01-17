from coord import Coord
from piece import Piece

class Game:
	def __init__(self):
		self.board = [[Piece() for x in range(8)] for y in range(8)]
		pieces = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
		currId = 0
		for i in range(8):
			self.board[0][i] = Piece(pieces[i], 1, currId, 0)
			currId+=1
		for i in range(8):
			self.board[1][i] = Piece("pawn", 1, currId, 0)
			currId+=1
		for i in range(8):
			self.board[6][i] = Piece("pawn", 0, currId, 0)
			currId+=1
		for i in range(8):
			self.board[7][i] = Piece(pieces[i], 0, currId, 0)
			currId+=1
		self.kings = [None,None]
		for c in [Coord(x,y) for x in range(8) for y in range(8)]:
			if self.getSquare(c).name == "king":
				self.kings[self.getSquare(c).team] = c
		
		self.turnCount = 0
		self.turn = 0
		self.SCORETHRESHOLD = 15
		self.log = []
		self.winner = -1
		
	
	def getPossibleMoves(self, c:Coord):
		if(c.isValid() == False):
			return -1
		p = self.getSquare(c)
		enemyTeam = 0 if p.team==1 else 1
		if p.name == "knight":
			deltas = [
				Coord(1,2),Coord(2,1),
				Coord(-1,2),Coord(-2,1),
				Coord(1,-2),Coord(2,-1),
				Coord(-1,-2),Coord(-2,-1),
			]
			out = []
			for delta in deltas:
				temp = c+delta
				if(temp.isValid() and self.getSquare(temp).team != p.team):
					out.append(temp)
			return out
		elif p.name == "king":
			deltas = [
				Coord(-1,0),Coord(-1,-1),
				Coord(0,-1),Coord(1,-1),
				Coord(1,0),Coord(1,1),
				Coord(0,1),Coord(-1,1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				if(temp.isValid() and self.getSquare(temp).team != p.team):
					out.append(temp)
			return out
		elif p.name == "rook":
			deltas = [
				Coord(-1,0),Coord(1,0),
				Coord(0,1),Coord(0,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "bishop":
			deltas = [
				Coord(-1,1),Coord(-1,-1),
				Coord(1,1),Coord(1,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "queen":
			deltas = [
				Coord(-1,0),Coord(1,0),
				Coord(0,1),Coord(0,-1),
				Coord(-1,1),Coord(-1,-1),
				Coord(1,1),Coord(1,-1)
			]
			out = []
			for delta in deltas:
				temp = c+delta
				while (temp.isValid() and self.getSquare(temp).team != p.team):
					if(self.getSquare(temp).team == enemyTeam):
						out.append(temp)
						break
					out.append(temp)
					temp = temp+delta
			return out
		elif p.name == "pawn":
			out = []

			forwards = Coord(0,1)
			if(p.team == 0):
				forwards = Coord(0,-1)
			if(self.getSquare(c+forwards).team == -1):
				out.append(c+forwards)
				if(p.timeMoved == 0 and self.getSquare(c+forwards+forwards).team == -1): 
					out.append(c+forwards+forwards)
			
			#capturing
			deltas = [Coord(-1, 0)+forwards, Coord(1, 0)+forwards]
			for delta in deltas:
				t = c+delta
				# print("Coord:",t)
				# print("Square:",self.getSquare(t))
				# print("Team:",self.getSquare(t).team)
				if t.isValid() and self.getSquare(t).team == enemyTeam:
					out.append(t)
			"""Add en passant if extra time"""
			return out
		raise Exception("Tried to get move at non piece square "+str(c))
	
	def updateKingPos(self):
		for c in [Coord(x,y) for x in range(8) for y in range(8)]:
			if self.getSquare(c).name == "king":
				self.kings[self.getSquare(c).team] = c

	def kingInCheck(self, team:int):
		enemy = 1 if team==0 else 0
		self.updateKingPos()
		kingC = self.kings[team]
		
		knightSquares = [
			Coord(-2, 1), Coord(-1,2),
			Coord(1, 2), Coord(2,1),
			Coord(2, -1), Coord(1,-2),
			Coord(-1, -2), Coord(-2,-1)
		]
		for tCoord in [kingC+delta for delta in knightSquares if (kingC+delta).isValid()]:
			if self.getSquare(tCoord).team == enemy and self.getSquare(tCoord).name == "knight":
				return True
		forward = -1 if team == 0 else 1
		pawnSquares = [
			Coord(-1, forward), Coord(1,forward)
		]
		
		for tCoord in [kingC+delta for delta in pawnSquares if (kingC+delta).isValid()]:
			# print(self.getSquare(tCoord))
			if self.getSquare(tCoord).team == enemy and self.getSquare(tCoord).name == "pawn":
				return True

		deltaDirs = [
			Coord(0, 1), Coord(1, 0), 
			Coord(0, -1), Coord(-1, 0)
		]
		for dir in deltaDirs:
			tCoord = kingC + dir
			while tCoord.isValid():
				if self.getSquare(tCoord).team==team:
					break
				if self.getSquare(tCoord).team==enemy:
					if self.getSquare(tCoord).name in ["rook", "queen"]:
						return True
					break
				tCoord = tCoord+dir

		deltaDirs = [
			Coord(1, 1), Coord(1, -1), 
			Coord(-1, 1), Coord(-1, -1)
		]
		for dir in deltaDirs:
			tCoord = kingC + dir
			while tCoord.isValid():
				if self.getSquare(tCoord).team==team:
					break
				if self.getSquare(tCoord).team==enemy:
					if self.getSquare(tCoord).name in ["bishop", "queen"]:
						return True
					break
				tCoord = tCoord+dir

		return False
		
	def checkValid(self, c:Coord, to:Coord):
		if(c == to):
			return False
		team = self.getSquare(c).team
		oldRef = self.getSquare(to)
		oldPiece = Piece(oldRef.name, oldRef.team, oldRef.id, oldRef.timeMoved)
		self.movePiece(c, to)
		
		out = not self.kingInCheck(team)
		# if out == True:
		# 	self.debugPrint()
		
		self.movePiece(to, c)
		self.setSquare(to, oldPiece)
		# if(out == True):
			# self.debugPrint()
		return out

	def isStaleMate(self, team):
		for tempC in [Coord(x,y) for x in range(8) for y in range(8)]:
			if(self.getSquare(tempC).team == team):
				if(len(self.getValidMoves(tempC))>0):
					# print(self.getSquare(tempC))
					# print(tempC,"can move to",[str(v) for v in self.getValidMoves(tempC)])
					return False
		return True

	def isCheckMate(self, team):
		if(self.kingInCheck(team)==False):
			return False
		for tempC in [Coord(x,y) for x in range(8) for y in range(8)]:
			if(self.getSquare(tempC).team == team):
				if(len(self.getValidMoves(tempC))>0):
					# print(self.getSquare(tempC))
					# print(tempC,"can move to",[str(v) for v in self.getValidMoves(tempC)])
					return False
		return True

	def getValidMoves(self, c:Coord):
		possible = self.getPossibleMoves(c)
		# print([str(x) for x in possible])
		out = []
		for move in possible:
			# print("Move:",move)
			if(self.checkValid(c, move)):
				# self.debugPrint()
				out.append(move)
		return out

	def movePiece(self, fromC:Coord, toC:Coord):
		# print("Moving from:",fromC)
		# print("Moving to  :",toC)
		if self.getSquare(fromC).name == "king":
			self.updateKingPos()
		elif self.getSquare(toC).name == "king":
			self.updateKingPos()
		self.setSquare(toC, self.getSquare(fromC))
		self.setSquare(fromC, Piece())
		
	def checkRepetition(self):
		if len(self.log)<6:
			return False
		count = self.log.count(self.log[-1])
		if count<3:
			return False
		count = self.log.count(self.log[-2])
		if count<3:
			return False
		return True

	def checkInactivity(self):
		if len(self.log)<50:
			return False
		val = self.log[-1][3]
		for i in range(49):
			if(self.log[-i][4] != val):
				return False
		return True

	def getSquare(self, c:Coord):
		if(c.isValid() == False):
			raise Exception("Invalid get, out of bounds: Tried to get at "+str(c))
		return self.board[c.y][c.x]
	
	def setSquare(self, c:Coord, p:Piece):
		if(c.isValid() == False):
			raise Exception("Invalid set, out of bounds: Tried to get at "+str(c))
		self.board[c.y][c.x] = Piece(p.name, p.team, p.id, p.timeMoved)

	def makeMove(self, fromC:Coord, toC:Coord): #True if move went through
		self.updateWinner()
		# try:
		if toC not in self.getValidMoves(fromC):
			return False
		# except Exception as e:
		# 	print("ISSUE AT MAKE MOVE:",e)
		# 	return False
		print("Recieved move request")
		print(fromC)
		print(toC)
		if(self.getSquare(fromC).team != self.turn):
			return False

		self.turnCount+=1
		self.movePiece(fromC, toC)
		self.log.append([fromC, toC, self.getSquare(toC).id, self.getScore()])
		self.board[toC.y][toC.x].timeMoved = self.turnCount
		queeningRank = 8*self.getSquare(toC).team
		if self.getSquare(toC).name == "pawn" and toC.y == queeningRank:
			self.board[toC.y][toC.x].name = "queen"
		self.turn = 0 if self.turn == 1 else 1
		self.updateWinner()
		return True

	def getScore(self):
		pointVals = {
			"queen" :9,
			"rook"  :5,
			"bishop":3,
			"knight":3,
			"pawn"  :1,
			"king"  :0
		}
		total = 0
		for c in [Coord(x,y) for x in range(8) for y in range(8)]:
			t = self.getSquare(c)
			if t.team == 1:
				total+=pointVals[t.name]
			elif t.team == 0:
				total-=pointVals[t.name]

		return total
	
	def updateWinner(self):
		if self.winner == -1:
			if self.checkWin():
				self.winner = self.turn

	def checkWin(self):
		current = self.turn
		if self.checkRepetition():
			print("Win by repetition")
			return True
		if self.checkInactivity():
			print("Win by inactivity")
			return True
		if self.isCheckMate(current):
			print("Win by checkmate")
			return True
		if self.isStaleMate(current):
			print("Win by stalemate")
			return True
		scoreMod = 1 if current == 0 else -1
		if scoreMod*self.getScore() > self.SCORETHRESHOLD:
			print("Win by score")
			return True
		return False
		
	
	def debugPrint(self):
		for row in self.board:
			for val in row:
				if(val.team!=-1):
					print(val.name[0],end="")
				else:
					print(" ",end="")
			print()
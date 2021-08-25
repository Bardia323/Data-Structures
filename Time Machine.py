# Here is a universally applicable time machine in python with rewind and branching universes.
# Time machines are useful for simulating the past, present, and future.
#
# - games
# - simulations
# - video editing
# - time-dependent calculations
# - stocks and bonds

class TimeMachine:

	def __init__(self):
		self.queue = []
		self.branched_universes = []
		self.symbol_table = []
		self.default_symbol_table = {}
	
	def set(self, symbol, value):
		self.default_symbol_table[symbol] = value
	
	def tick(self):
		if self.queue:
			symbol, value = self.queue.pop(0)
			self.symbol_table.insert(0, self.default_symbol_table)
			self.symbol_table[0][symbol] = value
		else:
			self.symbol_table.insert(0, self.default_symbol_table)
		self.branched_universes.insert(0, {})
	
	def tock(self):
		self.symbol_table.pop(0)
		self.branched_universes.pop(0)
	
	def branch(self):
		branch = TimeMachine()
		# copy symbol table
		branch.symbol_table = []
		for _ in range(len(self.symbol_table)):
			branch.symbol_table.append(self.symbol_table.pop())
		self.branched_universes.pop()
		return branch
	
	def back(self):
		if self.branched_universes:
			self.symbol_table = self.symbol_table[:-1]
			self.branched_universes = self.branched_universes[:-1]
	
	def forward(self):
		if self.branched_universes:
			self.symbol_table.append(self.symbol_table.pop(0))
			self.branched_universes.append(self.branched_universes.pop(0))
	
	def get(self, symbol):
		for _ in range(len(self.symbol_table)):
			if symbol in self.symbol_table[_]:
				return self.symbol_table[_][symbol]

class TimeMachineWorkbench:

	def __init__(self):
		self.machine = TimeMachine()
	
	def set(self, symbol, value):
		self.machine.set(symbol, value)
	
	def tick(self):
		self.machine.tick()
	
	def tock(self):
		self.machine.tock()
	
	def branch(self):
		return self.machine.branch()
	
	def back(self):
		self.machine.back()
	
	def forward(self):
		self.machine.forward()
	
	def get(self, symbol):
		return self.machine.get(symbol)
	
	def __del__(self):
		del self.machine

x = TimeMachineWorkbench()
x.set('a', 1)
x.set('a', 2)
x.tick()
x.tock()
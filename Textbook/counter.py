class Counter:

    def __init__(self):
        self.theCount = 0

    def inc(self):
        if self.theCount < 9999:
            self.theCount = self.theCount + 1
        else:
            self.theCount = 0

    def dec(self):
        if self.theCount > 0:
            self.theCount = self.theCount - 1
        else:
            self.theCount = 9999

    def getCount(self):
        return self.theCount

    def setCount(self, newCount):
        self.theCount = newCount

    def equals(self, other):
        return self.theCount == other.theCount
    def update (self, qty):
        self.theCount += qty


X = "aabbcc"

A = Counter ()
B = Counter ()
C = Counter ()
D = C
E = B

A.inc()

for char in X :
    A.inc()

B.dec()
B.dec()

B.dec()
B.inc()

C.inc()
C.setCount(7)

# AFTER RUNNING ALL OF THE CODE ABOVE

# How many times was the body of the for loop above executed ? 6

# What is the value of char ? c

# What is the value of A.getCount() ? 7

# What is the value of B.getCount() ? 998

# What is the value of E.getCount() ? 998

# What is the value of C.getCount() ? 7

# What is the value of C == D ? True

# What is the value of A == C ? False

# What is the value of A.equals(C) ? True
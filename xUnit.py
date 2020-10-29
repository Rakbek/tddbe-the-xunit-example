class WasRun:
    def __init__(self, name):
        self.WasRun = None
        self.name = name
    def testMethod(self):
        self.WasRun = 1
    def run(self):
        method = getattr(self, self.name)
        method()

test = WasRun("testMethod")
print (test.WasRun)
test.run()
print (test.WasRun)
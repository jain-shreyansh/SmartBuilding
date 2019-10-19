class Structure:
    def __init__(self, parent=None):
        self.children = {}
        self.parent = parent
        self.funcs = []

    def addChild(self, key, child):
        self.children[key] = child
    
    def addFunction(self, func):
        self.funcs.append(func)
    
    def runFrame(self):
        for func in funcs:
            if func == None:
                pass
            func()
    
    
    
    
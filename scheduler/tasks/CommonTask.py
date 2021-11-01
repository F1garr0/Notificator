
class CommonTask(object):
    locked = True

    def execute(self):
        if self.locked:
            self.checkToUnlock()
        else:
            pass
    
    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True

    def checkToUnlock(self):
        pass
    
    def configure(self, params):
        pass

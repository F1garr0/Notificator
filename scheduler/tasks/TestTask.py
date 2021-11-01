from .CommonTask import CommonTask

class TestTask(CommonTask):
    
    text = "Hello world"

    def execute(self):
        print("Executing test task")
        print(self.text)

    def configure(self, params):
        self.text = params


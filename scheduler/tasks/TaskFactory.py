from scheduler.tasks.TGUserNotification import TGUserNotification
from .CommonTask import CommonTask
from .TestTask import TestTask


class TaskFactory(object):

    @staticmethod
    def getTask(taskName : str):
        if taskName.__eq__("test"):
            return TestTask()
        if taskName.__eq__("tg"):
            return TGUserNotification()

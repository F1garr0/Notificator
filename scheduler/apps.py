from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.tasks.CommonTask import CommonTask
from scheduler.tasks.TaskFactory import TaskFactory
from scheduler.tasks.TestTask import TestTask

class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from api.models import UserTask, TaskConfig
        scheduler = BackgroundScheduler({'apscheduler.timezone': 'UTC'})
        scheduler.start()
        task : UserTask
        for task in UserTask.objects.all():
            job : CommonTask | None  = TaskFactory.getTask(task.task_name)
            print("==================================")
            print(task.task_name)
            if job:
                config = TaskConfig.objects.get(id=2)
                #print(config)
                job.configure(309860489)
                scheduler.add_job(job.execute, 'interval', minutes = 1)
       
        print("Scheduler started")

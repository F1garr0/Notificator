
from scheduler.tasks.CommonTask import CommonTask
from pyrogram import Client, filters

class TGUserNotification(CommonTask):
   
    def execute(self):
        print("TG -> trying to create tg client")
        app = Client("my", self.api_id, self.api_hash)
        print("TG -> Connecting")
        connected = app.connect()
        print(connected)
        print("TG -> connected")
        user = app.get_users( 309860489 )
        print(user)
        print(user.status)
        app.disconnect()

        #with Client("my_account", self.api_id, self.api_hash) as app:
        #    print("executing TG TASK")
                #app.send_message("me", "Greetings from **Pyrogram**!")
        #    print(app.get_user(self.user_id).status)
                #if app.get_user(params).status != 'offline':
                #   print("user online")

    def configure(self, params):
        self.user_id = params

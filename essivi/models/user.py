from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    username = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_user_by_username(username):
        try:
            return User.objects.get(username= username)
        except:
            return False


    def isExists(self):
        if User.objects.filter(username = self.username):
            return True

        return False
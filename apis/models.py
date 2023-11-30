from django.db import models


class UserMaster(models.Model):
    user_id = models.AutoField(primary_key=True)
    uer_name = models.CharField(max_length=100)
    user_mobile_number = models.IntegerField()
    user_address = models.CharField(max_length=250)
    user_parmanent_address = models.CharField(max_length=250)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "user_master"

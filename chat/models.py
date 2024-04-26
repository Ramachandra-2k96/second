from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Notificaton_Model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=100)
    is_like = models.BooleanField(default=False)
    
    def save(self,*args,**kwargs):
        channel_layer = get_channel_layer()
        notification_object = Notificaton_Model.objects.filter(is_like=False).count()
        data ={'count':notification_object,'current_notificatopn':self.message}
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',{
                'type':'send_notification',
                'value':json.dumps(data),
            }
            )
        super(Notificaton_Model,self).save(*args,**kwargs)
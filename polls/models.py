import datetime
from django.utils import timezone

# Create your models here.
from django.db import models

class Poll(models.Model):
  
  question = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date_published')
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
  
  def __unicode__(self):
    return self.question
  
  was_published_recently.admin_order_field = 'pub_date'
  was_published_recently.boolean = True
  was_published_recently.short_description = "Published Recently?"
  
class Choice(models.Model):
  
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  
  def __unicode__(self):
    return self.choice_text
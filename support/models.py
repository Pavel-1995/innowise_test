from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    """Class create ticket"""
    class Status(models.IntegerChoices):
        """Class choice status"""
        waiting_for_a_question = 0
        in_processing = 1
        processed = 2
        unopened = 3

    text_ticket = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creation time")
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status.choices, default=Status.waiting_for_a_question)

    def __str__(self):
        """Display ticket"""
        return self.text_ticket


class Message(models.Model):
    """Class answer"""
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Creation time")
    number_ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text_answer = models.TextField(blank=False)

    def __str__(self):
        """Display answer"""
        return self.text_answer

from django.db import models
from django.conf import settings
from django.utils import timezone


INBOX_MESSAGE_TYPES = (
    ('GE_MSG', 'General messages'),
    ('VISIT', 'Messages from visit'),
    ('PATIENT', 'Messages from patients'),
    ('SYS_MSG', 'System Messages')
)


class UsersQuestion(models.Model):
    question = models.CharField(max_length=255)
    response = models.TextField()
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='user_questions')


class UsersGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="user_groups")


class MessageAbstractBase(models.Model):

    content_string = models.TextField(null=False, blank=True)
    message_type = models.CharField(
        max_length=12,
        choices=INBOX_MESSAGE_TYPES, default="GE_MSG"
    )
    read = models.BooleanField(default=False)
    url = models.URLField(default=None, blank=True, null=True)
    item_id = models.CharField(max_length=100, blank=True, null=True)
    action_taken = models.CharField(max_length=20, blank=True, null=True)
    sent_date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100, null=True, blank=True)

    class Meta(object):
        abstract = True
        ordering = ('read',)


class UserMessage(MessageAbstractBase):

    """
    Contains messages associated with a user
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return "Inbox: %s" % (self.user.get_full_name())


class GroupMessage(MessageAbstractBase):
    """
    A 'group' is any set of users that have the same action e.g all users with
    an action that permits them to 'Send a Pre-Authorization Request' are a
    group

    """
    group = models.ForeignKey(UsersGroup, on_delete=models.PROTECT)

    def __str__(self):
        return "Group Message: %s" % (self.group)

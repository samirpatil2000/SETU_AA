from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(db_index=True, max_length=10, unique=True)

    def __str__(self):
        return self.name + " <=> " + self.phone_number


class Consent(BaseModel):
    consent_id = models.CharField(max_length=40, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    redirect_url = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name + " <=> " + self.consent_id


class Sessions(BaseModel):
    sessions_id = models.CharField(max_length=40, unique=True, db_index=True)
    consent = models.OneToOneField(Consent, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    notification_response = models.TextField(blank=True, null=True)
    session_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.consent) + " <=> " + self.sessions_id
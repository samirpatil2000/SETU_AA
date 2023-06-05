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


class Consent(BaseModel):
    consent_id = models.CharField(max_length=40, unique=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    redirect_url = models.CharField(max_length=100)

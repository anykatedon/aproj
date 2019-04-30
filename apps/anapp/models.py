from django.db import models


# Create your models here.
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=255)

    def __str__(self):
        return self.doctor_name


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='feedback')
    patient_name = models.CharField(max_length=255)
    email = models.EmailField()
    details = models.TextField()
    satisfied = models.BooleanField(default=False)
    feedback_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

    class Meta:
        verbose_name_plural = 'feedback'

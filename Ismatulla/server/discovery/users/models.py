from django.db import models
from django.contrib.auth.models import AbstractUser
from users.functions import (user_default_pro_pic,
                             user_dir, file_size, generate_ref_code)


class User(AbstractUser):
    first_name = models.CharField(
        max_length=50, verbose_name="First Name")
    last_name = models.CharField(
        max_length=50, verbose_name="Last Name")

    # the first option in the dropdown
    GENDER_CHOICES = [('', 'Select'), ('F', 'Female'),
                      ('M', 'Male'), ('O', 'Other')]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, )

    # Using verbose_name in the form.
    pro_pic = models.ImageField(default=user_default_pro_pic,
                                upload_to=user_dir,
                                verbose_name="Profile Picture",
                                validators=[file_size])

    recommended_by=models.ForeignKey("User", on_delete=models.CASCADE, blank=True, null=True)
    ref_code=models.CharField(max_length=50, blank=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    # Overriding the save method
    def save(self, *args, **kwargs):
        if self.ref_code=="":
            ref_code=generate_ref_code()
            self.ref_code=ref_code
        super().save(*args, **kwargs)

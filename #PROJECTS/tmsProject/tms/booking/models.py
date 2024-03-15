from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    ID_TYPES = [
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
        ('national_id', 'National ID'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    alternative_phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    id_type = models.CharField(max_length=20,choices=ID_TYPES)
    id_image = models.ImageField(upload_to='user_use')

    def __str__(self):
        return f'{self.user.username} Profile'


class DestinationCategory(models.Model):
    cat_name = models.CharField(max_length=45)

    def __str__(self):
        return self.cat_name

class Destination(models.Model):
    des_name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='admin_use')
    des_category = models.ForeignKey(DestinationCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.des_name


class CMSPages(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Transportation(models.Model):
    t_type = models.CharField(max_length=10)
    details = models.CharField(max_length=255)

    def __str__(self):
        return self.t_type


class Destination(models.Model):
    des_name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='admin_use')
    des_category = models.ForeignKey(DestinationCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.des_name


class TripRoot(models.Model):
    start_place = models.CharField(max_length=45)
    end_place = models.CharField(max_length=45)
    pickup_point = models.CharField(max_length=45)
    drop_point = models.CharField(max_length=45)
    cost = models.CharField(max_length=100)
    gst_charge = models.CharField(max_length=100)
    cms_page = models.ForeignKey(CMSPages, on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Package(models.Model):
    p_name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    image = models.ImageField(upload_to='admin_use')
    description = models.CharField(max_length=255)
    start_place = models.CharField(max_length=45)
    end_place = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration_days = models.IntegerField()
    category = models.CharField(max_length=45)
    cost = models.CharField(max_length=100)
    cms_page = models.ForeignKey(CMSPages, on_delete=models.CASCADE)
    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_name


class Member(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.full_name


class CartItem(models.Model):
    no_of_members = models.CharField(max_length=45)
    payment_method = models.CharField(max_length=20)
    booking_status = models.CharField(max_length=20)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Cart item for {self.user_profile}"
    

class Booking(models.Model):
    no_of_members = models.CharField(max_length=45)
    payment_method = models.CharField(max_length=20)
    booking_status = models.CharField(max_length=20)
    additional_booking_details = models.TextField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    destinations = models.ManyToManyField(Destination)

    def __str__(self):
        return f"Booking for {self.user_profile}"
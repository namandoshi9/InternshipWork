from django.contrib import admin
from .models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]


@admin.register(CMSPages)
class CMSPagesAdmin(admin.ModelAdmin):
     list_display = [field.name for field in CMSPages._meta.fields]

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
     list_display = [field.name for field in Transportation._meta.fields]

    

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
     list_display = [field.name for field in Package._meta.fields]

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
     list_display = [field.name for field in Member._meta.fields]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
     list_display = [field.name for field in CartItem._meta.fields]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]


@admin.register(DestinationCategory)
class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DestinationCategory._meta.fields]


@admin.register(Destination)
class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Destination._meta.fields]
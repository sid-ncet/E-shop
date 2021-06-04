from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    catagory=models.ForeignKey('Catagory',on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200, default='')
    image=models.ImageField(upload_to='upload/products/')

class Catagory(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.IntegerField(default=0)
    password=models.CharField(max_length=40)

    def register(self):
        self.save()
    @ staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

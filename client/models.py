from django.db import models
from django.db.models.base import Model


# Create your models here.
# for list of bank names 
class BankName(models.Model):
    
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("BankName")
        verbose_name_plural = ("BankNames")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("BankName_detail", kwargs={"pk": self.pk})




class ClientDetail(models.Model):
    
    
    title                           = models.CharField(max_length=100)
    first_name                      = models.CharField(max_length=100)
    surname                         = models.CharField(max_length=100)
    other_name                      = models.CharField(max_length=100)
    phone_number                    = models.CharField(max_length=100)
    address                         = models.CharField(max_length=100)
    company_name                    = models.CharField(max_length=100)
    company_address                 = models.CharField(max_length=100)
    means_of_identification_choice   = (('drivers license','drivers license'),
                            ('international passport','international passport'),
                            ('voters card','voters card'),
                            ('others','others'),                            
                            
                            )
    means_of_identification         = models.CharField(choices = means_of_identification_choice,max_length=255,blank=True,null=True )
    identification_number           = models.CharField(max_length=100)
    PFA                             = models.CharField(max_length=100)
    RSA                             = models.CharField(max_length=100)
    
    will_executors_choice   = (('meristem trustees','meristem trustees'),
                            ('others','others'),
                           
                            )
    will_executors                  = models.CharField(choices = will_executors_choice,max_length=255,blank=True,null=True )
    options                         = models.CharField(max_length=100)
    
    # bank details 
    
    bank_name = models.ForeignKey(BankName, on_delete=models.CASCADE,blank=True,null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    
    # for adding more bank details 
    
    bank_name_2 = models.ForeignKey(BankName,related_name='Bank', on_delete=models.CASCADE,blank=True,null=True)
    account_number_2 = models.CharField(max_length=100, blank=True, null=True)
    branch_2 = models.CharField(max_length=100, blank=True, null=True)
    
    # beneficiary 
    
    full_name                   = models.CharField(max_length=100, blank=True, null=True)
    address_beneficiary         = models.CharField(max_length=100, blank=True, null=True)
    phone_number_beneficiary    = models.CharField(max_length=100, blank=True, null=True)
    bank_name_beneficiary       = models.CharField(max_length=100, blank=True, null=True)
    email                       = models.EmailField(max_length=255,blank=True,null=True)
    values                      = models.IntegerField(blank=True,null=True)
    # for adding more beneficiary details 
    
    full_name_2       = models.CharField(max_length=100, blank=True, null=True)
    address_beneficiary_2         = models.CharField(max_length=100, blank=True, null=True)
    phone_number_beneficiary_2    = models.CharField(max_length=100, blank=True, null=True)
    bank_name_beneficiary_2       = models.CharField(max_length=100, blank=True, null=True)
    email_2                       = models.EmailField(max_length=255,blank=True,null=True)
    values_2                     = models.IntegerField(blank=True,null=True)


    # time and date created 
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        verbose_name = ("Client Detail")
        verbose_name_plural = ("Client Details")

    def __str__(self):
        return f'{self.title} {self.first_name} {self.surname}'

    # def get_absolute_url(self):
    #     return reverse("ClientDetail_detail", kwargs={"pk": self.pk})

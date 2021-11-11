from django.db import models

# Create your models here.


# Bank details 

class BankDetail(models.Model):
    
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    
    # for adding more bank details 
    
    bank_name_2 = models.CharField(max_length=100, blank=True, null=True)
    account_number_2 = models.CharField(max_length=100, blank=True, null=True)
    branch_2 = models.CharField(max_length=100, blank=True, null=True)

   
    class Meta:
        verbose_name = ("Bank Detail")
        verbose_name_plural = ("Bank Details")

    def __str__(self):
        return self.bank_name

    # def get_absolute_url(self):
    #     return reverse("BankDetail_detail", kwargs={"pk": self.pk})

# Beneficiary Details 

class BeneficiaryDetail(models.Model):
    
    full_name                   = models.CharField(max_length=100)
    address_beneficiary         = models.CharField(max_length=100)
    phone_number_beneficiary    = models.CharField(max_length=100)
    bank_name_beneficiary       = models.CharField(max_length=100)

    # for adding more beneficiary details 
    
    full_name_2       = models.CharField(max_length=100)
    address_beneficiary_2         = models.CharField(max_length=100)
    phone_number_beneficiary_2    = models.CharField(max_length=100)
    bank_name_beneficiary_2       = models.CharField(max_length=100)

 

    class Meta:
        verbose_name = ("Beneficiary Detail")
        verbose_name_plural = ("Beneficiary Details")

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("BeneficiaryDetail_detail", kwargs={"pk": self.pk})


class ClientDetail(models.Model):
    
    title                           = models.CharField(max_length=100)
    first_name                      = models.CharField(max_length=100)
    surname                         = models.CharField(max_length=100)
    other_name                      = models.CharField(max_length=100)
    phone_number                    = models.CharField(max_length=100)
    address                         = models.CharField(max_length=100)
    company_name                    = models.CharField(max_length=100)
    company_address                 = models.CharField(max_length=100)
    means_of_identification_choice   = ((1,'drivers license'),
                            (2,'international passport'),
                            (3,'voters card'),
                            (4,'others'),                            
                            
                            )
    means_of_identification         = models.PositiveSmallIntegerField(choices = means_of_identification_choice,blank=True,null=True )
    identification_number           = models.CharField(max_length=100)
    PFA                             = models.CharField(max_length=100)
    RSA                             = models.CharField(max_length=100)
    address                         = models.CharField(max_length=100)
    will_executors_choice   = ((1,'meristem trustees'),
                            (2,'others'),
                           
                            )
    will_executors                  = models.PositiveSmallIntegerField(choices = will_executors_choice,blank=True,null=True )
    options                         = models.CharField(max_length=100)
    
    bank_details                    = models.ForeignKey(BankDetail,on_delete=models.CASCADE)
    beneficiary_details             = models.ForeignKey(BeneficiaryDetail,on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = ("Client Detail")
        verbose_name_plural = ("Client Details")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("ClientDetail_detail", kwargs={"pk": self.pk})

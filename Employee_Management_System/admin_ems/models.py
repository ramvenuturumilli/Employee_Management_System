from django.db import models


# Create your models here.
class user_table (models.Model):
   user_name = models.CharField(max_length=20, help_text='Enter user_name')
   first_name = models.CharField(max_length=20, help_text='Enter first_name')
   last_name = models.CharField(max_length=20, help_text='Enter last_name')
   number = models.CharField(max_length=20,help_text='Enter number')
   email = models.EmailField(max_length=25,help_text='Enter email')
   designation = models.CharField(max_length=20, help_text='Enter designation')
   department = models.CharField(max_length=20, help_text='Enter department')
   

#    #Metadata
#    class Meta :
#        ordering = [' user_table']

#    #Methods
#    def get_absolute_url(self):
#        return reverse('url', args=[args])

   def __str__(self):
       return self.user_name
    
class user_auth(models.Model):
    """Model definition for user_auth."""
    user_name = models.CharField(max_length=20, help_text='Enter user_name')
    emailField = models.CharField(max_length=20, help_text='Enter emailField')
    password = models.CharField(max_length=20, help_text='Enter password')
    # TODO: Define fields here

    class Meta:
        """Meta definition for user_auth."""

        verbose_name = 'user_auth'
        verbose_name_plural = 'user_auths'

    def __str__(self):
        """Unicode representation of user_auth."""
        return self.user_name


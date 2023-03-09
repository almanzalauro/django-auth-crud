from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    #auto_now_add=true para que me ponga la fecha en la que fue creada la tarea
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    #marco default=false para que no me las marque por defecto, yo soy el que las marca
    important = models.BooleanField(default=False)
    #relaciono cada user con User, y aplico eliminacion en cascada con on_delete=models.CASCADE 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #me muestra el titulo de la tarea y a que usuario pertenece
    def __str__(self):
        return self.title + '- by ' + self.user.username
    

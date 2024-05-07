from django.db import models

class Task(models.Model):
    class TaskChoices(models.TextChoices):
        NEW = 'new', 'New'
        INPROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    status = models.CharField(max_length=100, 
                            choices=TaskChoices.choices,
                            default=TaskChoices.NEW)


    def __str__(self) -> str:
        return f"{self.id} - {self.title}"
    


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_data = models.DateField()

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"




class Items(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    





# *******************metsenat*******************


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updataed_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Sponsor(BaseClass):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    organization = models.CharField(max_length=100)
   
    class SponsorTypeChoices(models.TextChoices):
        YURIDIC = 'yuridik', 'Yuridik'
        JISMONIY = 'jismoniy', 'Jismoniy'
   
    class StatusChoices(models.TextChoices):
        NEW = 'new', 'New'
        CONFIRM = 'confirm', 'Confirm'
        CENCELED = 'cenceled', 'Cenceled'
        MODERATION = 'moderation', 'Modiration'

  

class University(BaseClass):
    title = models.CharField(max_length=100)

  
    

class Student(BaseClass):
    class TypeChoices(models.TextChoices):
        MASTER = 'magster', 'Magister'
        BAKALAVR = 'bakalavr', 'Bakalavr'
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True)
    student_type = models.CharField(max_length=100, choices=TypeChoices.choices, default=TypeChoices.BAKALAVR)
    contract = models.DecimalField(max_digits=7, decimal_places=2)

    

class StudentSponser(BaseClass):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
from django.contrib import admin
from .models import Task, Person, Items, BaseClass, University, Sponsor, Student, StudentSponser

admin.site.register(Task)
admin.site.register(Person)
admin.site.register(Items)

admin.site.register(University)
admin.site.register(Sponsor)
admin.site.register(StudentSponser)
admin.site.register(Student)




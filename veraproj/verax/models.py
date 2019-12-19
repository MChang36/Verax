from django.db import models
from django.db.models.signals import post_save

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=250)
    average = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)

    # irrelevent
    def changeAverage(self, amt):
        if self.average is None:
            print("true")
            self.average = amt
            self.save(update_fields=['average'])
        else:
            print("false")
            self.average = (self.average + amt)/2
            self.save(update_fields=['average'])

    #unused
    def calculated_ave(self):
        my_tests = Test.objects.all().filter(student=self)
        if my_tests.count() is 0:
            return 0;
        else:
            print(my_tests)
            sum = 0
            for test in my_tests:
                sum += test.grade
            ave = sum / my_tests.count()
            return ave


    def __str__(self):
        return self.name

#unused
def updateAverage(instance, created, **kwargs):
    if created:
        student = instance.student
        print('hello')
        student.changeAverage(instance.grade)

class Test(models.Model):
    name = models.CharField(max_length=250)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return "{}-{}".format(self.student, self.name)

#unused
post_save.connect(updateAverage, sender=Test)
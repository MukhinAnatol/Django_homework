from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    teach_order = 'subject'
    students = Student.objects.order_by(ordering)
    teachers_all = Teacher.objects.order_by(teach_order)
    context = {'object_list': students,
               'teach_list': teachers_all}
    return render(request, template, context)

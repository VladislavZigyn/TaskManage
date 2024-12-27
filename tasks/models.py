from django.db import models

class Category (models.Model):

    title = models.CharField(max_length=80, verbose_name='Category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Tasks(models.Model):

    title = models.CharField(max_length=100, verbose_name='Task')
    description = models.TextField(blank=True, null=True, verbose_name='Details')
    task_date = models.DateTimeField(auto_now=True, verbose_name='Date of Creation')
    is_done = models.BooleanField(default=False, verbose_name='Done')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categories')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Objectives'
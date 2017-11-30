# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

CAMPUS_CHOICES = [
    ("seattle", "Seattle Campus"),
    ("tacoma", "Bothell Campus"),
    ("bothell", "Tacoma Campus")
]

STATUS_CHOICES = [
    ("open", "Open Admission"),
    ("minimum", "Minimum Requirements Admission"),
    ("capacity-constrained", "Capacity-contrained Admission")
]


class Major(models.Model):
    # assumption: major_abbr won't be longer than 15 chars
    major_abbr = models.CharField(max_length=15)
    # since empty pathways are not allowed, it defaults to 0
    pathway = models.IntegerField(default=0)
    # campus has to be one from the choices specified in CAMPUS_CHOICES
    campus = models.CharField(choices=CAMPUS_CHOICES, max_length=30)
    # assumption: no college and major_full_nm with length > 100
    college = models.CharField(max_length=100)
    major_full_name = models.CharField(max_length=100)
    url = models.CharField(blank=True, max_length=150)
    # status has to be one from the choices specified in STATUS_CHOICES
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)

    def __str__(self):
        return self.major_full_name


class GPA(models.Model):
    # model which identifies with major for a particular year
    # links to MajorDetails
    # contains gpa specific info only

    # CONNECT TO MAJOR DETAILS MODEL
    major = models.ForeignKey(
        Major,
        related_name='major_gpas',
        on_delete=models.CASCADE
    )
    year = models.IntegerField()
    # all decimals are between 0.00 - 4.00
    # interquartile minimum gpa
    iqr_min = models.DecimalField(max_digits=3, decimal_places=2)
    # quartile 1 gpa
    q1 = models.DecimalField(max_digits=3, decimal_places=2)
    # median gpa
    median = models.DecimalField(max_digits=3, decimal_places=2)
    # quartile 3 gpa
    q3 = models.DecimalField(max_digits=3, decimal_places=2)
    # interquartile maximum gpa
    iqr_max = models.DecimalField(max_digits=3, decimal_places=2)


class Course(models.Model):
    # model which identifies with major for a particular year
    # links to MajorDetails
    # contains course specific info

    # CONNECT A LIST OF THIS TO MAJOR DETAILS MODEL
    major = models.ForeignKey(
        Major,
        related_name='major_courses',
        on_delete=models.CASCADE
    )
    year = models.IntegerField()
    # assumption: dept_abbr won't be longer than 15 chars
    dept_abbr = models.CharField(max_length=15)
    course_number = models.IntegerField()
    student_count = models.IntegerField()
    students_in_major = models.IntegerField()
    # popularity_rank of course for given major
    popularity_rank = models.IntegerField()
    course_full_name = models.CharField(max_length=100)
    # percentiles are never queried, they are returned as is
    # stored as a stringified dict of key-val pairs using "repr"
    # can be converted back to a dict object with "eval"
    percentiles = models.CharField(max_length=150)

    def __str__(self):
        return self.course_full_name

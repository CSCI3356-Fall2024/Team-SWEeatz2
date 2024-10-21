from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GRADUATION_YEAR_CHOICES = [
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
]

MAJOR_CHOICES = [
    ('N/A','N/A'),
    ('African and African Diaspora Studies', 'African and African Diaspora Studies'),
    ('Applied Physics', 'Applied Physics'),
    ('Art History', 'Art History'),
    ('Biochemistry', 'Biochemistry'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Classics', 'Classics'),
    ('Communication', 'Communication'),
    ('Computer Science', 'Computer Science'),
    ('Economics', 'Economics'),
    ('English', 'English'),
    ('Elementary Education','Elementary Education'),
    ('Environmental Geoscience', 'Environmental Geoscience'),
    ('Environmental Studies', 'Environmental Studies'),
    ('Film Studies', 'Film Studies'),
    ('French', 'French'),
    ('Geological Sciences', 'Geological Sciences'),
    ('German Studies', 'German Studies'),
    ('Global Public Health and the Common Good (CSON)', 'Global Public Health and the Common Good (CSON)'),
    ('Hispanic Studies', 'Hispanic Studies'),
    ('History', 'History'),
    ('Human-Centered Engineering', 'Human-Centered Engineering'),
    ('Independent Major', 'Independent Major'),
    ('International Studies', 'International Studies'),
    ('Islamic Civilization and Societies', 'Islamic Civilization and Societies'),
    ('Italian', 'Italian'),
    ('Linguistics', 'Linguistics'),
    ('Mathematics', 'Mathematics'),
    ('Management (CSOM)','Management (CSOM)'), 
    ('Music', 'Music'),
    ('Neuroscience', 'Neuroscience'),
    ('Nursing','Nursing'),
    ('Philosophy', 'Philosophy'),
    ('Physics', 'Physics'),
    ('Political Science', 'Political Science'),
    ('Psychology', 'Psychology'),
    ('Russian', 'Russian'),
    ('Slavic Studies', 'Slavic Studies'),
    ('Sociology', 'Sociology'),
    ('Studio Art', 'Studio Art'),
    ('Theatre', 'Theatre'),
    ('Theology', 'Theology')
]





class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(blank = True, null = True)
    school = models.CharField(max_length = 100)
    graduation_year = models.CharField(max_length=4, choices=GRADUATION_YEAR_CHOICES, default='2025')
    major = models.CharField(max_length=100, choices=MAJOR_CHOICES, default='Computer Science')
    major2 = models.CharField(max_length=100, choices=MAJOR_CHOICES, default='N/A')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

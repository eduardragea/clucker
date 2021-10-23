from django import forms
from django.test import TestCase
from microblogs.forms import PostForm
from microblogs.models import User, Post

class PostFormTest(TestCase):
    

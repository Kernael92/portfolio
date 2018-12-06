from django.test import TestCase
from .models import Developer,Repository


# Create your tests here.
# Set up method
class DeveloperTestClass(TestCase):
    def setUp(self):
        self.kernaeljoy = Developer(first_name = "Kernael", last_name = "Joy", userName = "kernaeljoy", email = "kerry@gmail.com")
    # testing for the instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kernaeljoy,Developer))
    # testing the save functionality
    def test_save_method(self):
        self.kernaeljoy.save_developer()
        developers = Developer.objects.all()
        self.assertTrue(len(developers) > 0)




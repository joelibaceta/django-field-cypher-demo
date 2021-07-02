from django.test import TestCase
from demo.models import Member

# Create your tests here.
class MemberTest(TestCase):
  def setUp(self):
    Member.objects.create(first_name='Jhon', last_name='Rambo', email='jhon@rambo.com', phone='928882233')
    Member.objects.create(first_name='Juan', last_name='Perez', email='juan@mail.com', phone='23424546')
    Member.objects.create(first_name='Charles', last_name='Woodman', email='charles@google.com', phone='242344553')
    Member.objects.create(first_name='Diane', last_name='Rustley', email='diane@mail.com', phone='93844943')

  

  def test_find_by(self):
    member = Member.objects.get(first_name='Jhon')
    print(member.first_name)
    self.assertEqual(member.first_name, 'Jhon')
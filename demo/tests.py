from django.test import TestCase

from demo.models import Member

# Create your tests here.
class MemberTest(TestCase):
    def setUp(self):
        Member.objects.create(first_name='Jhon', last_name='Rambo', email='jhon@rambo.com', phone='928882233')
        Member.objects.create(first_name='Jhon', last_name='Alex', email='jhon@alex.com', phone='928882232')
        Member.objects.create(first_name='Juan', last_name='Perez', email='juan@mail.com', phone='23424546')
        Member.objects.create(first_name='Charles', last_name='Woodman', email='charles@google.com', phone='242344553')
        Member.objects.create(first_name='Charles', last_name='Chaplin', email='charles@chapiln.com', phone='242344553')
        Member.objects.create(first_name='Diane', last_name='Rustley', email='diane@mail.com', phone='93844943')

    def test_create(self):
        member = Member.objects.create(first_name='Charles', last_name='Smith', email='charles@mail.com', phone='92823233')
        self.assertEqual(member.first_name, 'Charles')

    def test_all(self):
        member = Member.objects.first()
        self.assertEqual(member.first_name, 'Jhon')

    def test_get(self):
        member = Member.objects.get(first_name='Diane')
        self.assertEqual(member.first_name, 'Diane')

    def test_get_two_fields(self):
        member = Member.cipher.get(first_name='Charles', last_name='Woodman')
        self.assertEqual(member.last_name, 'Woodman')

    def test_find_by(self):
        member = Member.cipher.filter(first_name='Jhon').first()
        self.assertEqual(member.first_name, 'Jhon')

    def test_find_by_two_fields(self):
        member = Member.cipher.filter(first_name='Jhon', last_name='Alex')
        self.assertEqual(member.first().last_name, 'Alex')





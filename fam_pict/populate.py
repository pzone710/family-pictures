import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fam_pict.settings')

import django
django.setup()

from first_app.models import FamilyMembers

def populate():
    FamilyMembers.objects.get_or_create(first_name='Pison', last_name='Tio')
    FamilyMembers.objects.get_or_create(first_name='Sylvia', last_name='Tio')
    FamilyMembers.objects.get_or_create(first_name='Orly', last_name='Tio')
    FamilyMembers.objects.get_or_create(first_name='Orin', last_name='Tio')

if __name__ == '__main__':
    print('Populating..')
    populate()
    print('Complete!')

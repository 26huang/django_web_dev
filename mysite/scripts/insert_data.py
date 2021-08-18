"""
Run this within Django shell
$python manage.py shell
"""
from apps.main import models
from django.utils import timezone
from random import randint


def show_subject():
    return models.Subject.objects.all()


def add_subject(title='', content='', published=timezone.now()):
    new_subject = models.Subject(title=title, content=content, published=published)
    new_subject.save()


if __name__ == "__main__":
    print(show_subject())
    subject_id = randint(0, 100)
    add_subject(title='Title-{}'.format(subject_id), content='Content of subject id {}.'.format(subject_id))
    print(show_subject())
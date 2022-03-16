from re import A
import pytest
from ..models import Image
##

def test_image_creation(user,test_image,remove_test_data):

    assert isinstance(test_image,Image)
    assert test_image.author == user
    assert test_image.url.url == '/media/images_files/test_image.jpg'
    assert test_image.name == 'test_image.jpg'
    assert str(test_image) == 'test_image.jpg'

def test_image_fields(db, test_image, remove_test_data):
    assert [*test_image.__dict__] == ['_state', 'id', 'author_id', 'url', 'name', 'created_at', 'updated_at']
# def test_create_user(user, django_user_model):
    
#     users = django_user_model.objects.all()
#     assert(len(users) == 2)


# def test_change_password(user):
#     user.set_password('test123')
#     assert user.check_password('test123') is True

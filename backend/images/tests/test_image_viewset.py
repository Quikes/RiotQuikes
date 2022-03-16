from django.urls import reverse
import pytest

from rest_framework.test import force_authenticate
from rest_framework import status

from ..views import ImageViewset

#remove test data ostatni , zeby nie zrobil teardowna przed zakonczeniem


@pytest.mark.views
def test_user_can_see_own_image(user, test_image, api_rf, remove_test_data):

    view = ImageViewset.as_view({'get': 'list'})

    endpoint = 'api/v1/images/'

    request = api_rf.get(endpoint)

    force_authenticate(request, user)

    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0].get('id') == test_image.id
    assert response.data[0].get('name') == 'test_image.jpg'
    assert response.data[0].get('author') == user.id



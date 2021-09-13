import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse("aperitivos:video", args=("MM",)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1>Minnie The Moocher</h1>')


def test_video_content(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/603606638?h=d8f7b448cc"')

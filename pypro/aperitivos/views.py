from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.vimeo_id = vimeo_id
        self.titulo = titulo
        self.slug = slug

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('minnie-the-moocher', 'Minnie The Moocher', '603606638?h=d8f7b448cc'),
    Video('snow-white', 'Snow White', '604460418?h=f9fbd0a002'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

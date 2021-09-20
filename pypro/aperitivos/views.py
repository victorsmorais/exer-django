from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='minnie-the-moocher', titulo='Minnie The Moocher', vimeo_id='603606638?h=d8f7b448cc'),
    Video(slug='snow-white', titulo='Snow White', vimeo_id='604460418?h=f9fbd0a002'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})

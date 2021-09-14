from django.shortcuts import render


def video(request, slug):
    videos = {
         "minnie-the-moocher": {'titulo': 'Minnie The Moocher', 'vimeo_id': '603606638?h=d8f7b448cc'},
         "snow-white": {'titulo': 'Snow White', 'vimeo_id': '604460418?h=f9fbd0a002'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

from django.utils import translation


# This function translates as currnet language.
def translate(request):
    language_code = request.get_host().split('.')[0]  # 'en' or 'de' or 'fr'
    translation.activate(language_code)
    return language_code
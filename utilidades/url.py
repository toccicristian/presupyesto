def urlnorm(url=str()):
    for elemento in ['view-source:', 'http://view-source:', 'https://view-source:']:
        if url.startswith(elemento):
            url = url.lstrip(elemento)
    if not url.startswith('https://') and not url.startswith('http://'):
        url='https://'+url
    if url.startswith('http://'):
        if not url.lstrip('http://').startswith('www.'):
            url='http://www.'+(url.lstrip('http://'))
    if url.startswith('https://'):
        if not url.lstrip('https://').startswith('www.'):
            url='https://www.'+(url.lstrip('https://'))
    return url

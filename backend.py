def alldownloader(url_id):
    import json

    import requests

    url = "https://social-media-video-downloader.p.rapidapi.com/smvd/get/all"

    querystring = {"url": url_id,
                   "filename": "Test video"}

    headers = {
        "X-RapidAPI-Key": "c267409d5dmsh2e386983ac07a99p1f2307jsn27596f56a42b",
        "X-RapidAPI-Host": "social-media-video-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)

    if data['success'] == False:
        return 'xato'
    else:
        dict = {
            'video': data['links'][0]['link'],
            'title': data['title']
        }
        return dict

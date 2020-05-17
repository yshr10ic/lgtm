import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path

    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """キーワード検索で画像を取得する"""

    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')


KeywordImage = _LoremFlickr


def ImageSource(keyword):
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)

def get_image(keyword):
    return ImageSource(keyword).get_image()

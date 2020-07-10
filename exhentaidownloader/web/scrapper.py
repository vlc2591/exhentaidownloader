from requests import Response
import re

p_first_page_gallery = re.compile(r'<a href=\"(https\:\/\/exhentai\.org\/s\/\w+\/\w+\-1)\">')
p_gallery_title = re.compile(r'<h1 id="gn">(.*)<\/h1><h1 id="gj">')

def get_first_image_page_link(data: Response):
    return ""


def get_next_image_page_link(data: Response):
    return ""


def get_image_link(data: Response):
    return ""


def get_gallery_title(data: Response):
    match = p_gallery_title.search(data.text)
    if type(match) is re.Match:
        result = match.groups()[0]
    else:
        result = ""
    return result

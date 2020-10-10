from requests import Response
import re

p_first_page_gallery = re.compile(r'<a href=\"(https\:\/\/exhentai\.org\/s\/\w+\/\w+\-1)\">')
p_gallery_title = re.compile(r'<h1 id="gn">(.*)<\/h1><h1 id="gj">')
p_next_image_page = re.compile(r'<a id=\"next\" onclick=\"return load_image\(\d, \'\w+\'\)\" href=\"(https\S+)\"><img')
p_image_link = re.compile(r'<img id=\"img\" src=\"(\S+)\" style')
p_gallery_total_images = re.compile(r'<td class="gdt2">(\d+) pages</td>')


def get_first_image_page_link(data: Response):
    return __regex_search(p_first_page_gallery, data.text)


def get_next_image_page_link(data: Response):
    return __regex_search(p_next_image_page, data.text)


def get_image_link(data: Response):
    return __regex_search(p_image_link, data.text)


def get_gallery_title(data: Response):
    return __regex_search(p_gallery_title, data.text)


def get_number_of_images(data: Response):
    return int(__regex_search(p_gallery_total_images, data.text))


def __regex_search(pattern: re.Pattern, text: str):
    match = pattern.search(text)
    if type(match) is re.Match:
        result = match.groups()[0]
    else:
        result = ""
    return result

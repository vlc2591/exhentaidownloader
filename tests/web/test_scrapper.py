import os

from exhentaidownloader.web.scrapper import get_first_image_page_link, get_next_image_page_link, get_image_link
from tests.web.mock_response import MockResponse

test_files_path = os.path.abspath(os.path.dirname(__file__))


class TestScrapper:
    def test_retrieve_link_for_first_image_from_gallery(self):
        with open(f'{test_files_path}/gallery.html') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://exhentai.org/s/6f365a4f9b/574260-1'
        link = get_first_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_next_image_from_image_page(self):
        with open(f'{test_files_path}/image_middle_gallery.html') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://exhentai.org/s/ebc9f3feb8/574260-6'
        link = get_next_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_actual_image_from_image_page(self):
        with open(f'{test_files_path}/image_middle_gallery.html') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://gvvrlvv.gsvxzhxipxzi.hath.network/h/d9718fe632141993150f01daf36485c0e479114b-' \
                        '204981-915-1300-jpg/keystamp=1594053600-d7050905db;fileindex=27831497;xres=org/28bd81' \
                        'fc6280bc2fc82bfe1b0690bed6.jpg'
        link = get_image_link(mock_response)
        assert link == expected_link

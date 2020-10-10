import os

from exhentaidownloader.web.scrapper import get_first_image_page_link, get_next_image_page_link, get_image_link, \
    get_gallery_title, get_number_of_images
from tests.web.mock_response import MockResponse

test_files_path = os.path.abspath(os.path.dirname(__file__))


class TestScrapper:
    def test_retrieve_link_for_first_image_from_gallery(self):
        with open(f'{test_files_path}/gallery.html', 'rb') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://exhentai.org/s/6f365a4f9b/574260-1'
        link = get_first_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_first_image_from_gallery_but_not_found(self):
        data = b''
        mock_response = MockResponse(data, 200)
        expected_link = ''
        link = get_first_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_next_image_from_image_page(self):
        with open(f'{test_files_path}/image_middle_gallery.html', 'rb') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://exhentai.org/s/ebc9f3feb8/574260-6'
        link = get_next_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_next_image_from_image_page_but_not_found(self):
        data = b''
        mock_response = MockResponse(data, 200)
        expected_link = ''
        link = get_next_image_page_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_actual_image_from_image_page(self):
        with open(f'{test_files_path}/image_middle_gallery.html', 'rb') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_link = 'https://gvvrlvv.gsvxzhxipxzi.hath.network/h/d9718fe632141993150f01daf36485c0e479114b-' \
                        '204981-915-1300-jpg/keystamp=1594053600-d7050905db;fileindex=27831497;xres=org/28bd81' \
                        'fc6280bc2fc82bfe1b0690bed6.jpg'
        link = get_image_link(mock_response)
        assert link == expected_link

    def test_retrieve_link_for_actual_image_from_image_page_but_not_found(self):
        data = b''
        mock_response = MockResponse(data, 200)
        expected_link = ''
        link = get_image_link(mock_response)
        assert link == expected_link

    def test_get_title(self):
        with open(f'{test_files_path}/gallery.html', 'rb') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_title = 'High Heels'
        title = get_gallery_title(mock_response)
        assert title == expected_title

    def test_get_title_but_not_found(self):
        data = b''
        mock_response = MockResponse(data, 200)
        expected_title = ''
        title = get_gallery_title(mock_response)
        assert title == expected_title

    def test_get_title_with_japanese_one_is_present(self):
        with open(f'{test_files_path}/gallery_with_japanese_title.html', 'rb') as file:
            data = file.read()
        mock_response = MockResponse(data, 200)
        expected_title = '[hentaiworks (Aruma)] Futanari Sennou Kaizou Koujou 2/4 [Chinese]'
        title = get_gallery_title(mock_response)
        assert title == expected_title

    def test_get_total_number_of_images(self):
        with open(f'{test_files_path}/gallery.html', 'rb') as file:
            data_gallery_1 = file.read()
        mock_response_gallery_1 = MockResponse(data_gallery_1, 200)
        expected_number_images_gallery_1 = 252
        result_1 = get_number_of_images(mock_response_gallery_1)

        with open(f'{test_files_path}/gallery_with_japanese_title.html', 'rb') as file:
            data_gallery_2 = file.read()
        mock_response_gallery_2 = MockResponse(data_gallery_2, 200)
        expected_number_images_gallery_2 = 33
        result_2 = get_number_of_images(mock_response_gallery_2)

        assert result_1 == expected_number_images_gallery_1
        assert result_2 == expected_number_images_gallery_2

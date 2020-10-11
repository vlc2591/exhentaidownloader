import time

import pytest
from mock import Mock, patch, call

from exhentaidownloader.processor.gallery import GalleryProcessor
from exhentaidownloader.web.credentials import Credentials


class TestGalleryProcessor:

    def test_raise_exception_if_not_given_gallery_url_in_constructor(self):
        with pytest.raises(Exception) as ex:
            GalleryProcessor()
        assert str(ex.value) == 'Gallery url must be provided'

    def test_raise_exception_if_not_given_credential_in_constructor(self):
        with pytest.raises(Exception) as ex:
            GalleryProcessor('mock_url')
        assert str(ex.value) == 'Credentials object must be provided'

    @patch('exhentaidownloader.processor.gallery.obtain_document')
    @patch('exhentaidownloader.processor.gallery.get_gallery_title')
    @patch('exhentaidownloader.processor.gallery.get_number_of_images')
    @patch('exhentaidownloader.processor.gallery.get_first_image_page_link')
    def test_init_is_ok(self, mock_get_first_image, mock_get_number_images, mock_get_title, mock_obtain_document):
        mock_credentials = Credentials(Mock(), Mock())
        mock_url = 'mock_url'
        mock_first_image_url = 'mock_first_image_url'
        mock_total_number_images = 123
        mock_gallery_title = 'mock_gallery_title'
        mock_get_first_image.return_value = mock_first_image_url
        mock_get_number_images.return_value = mock_total_number_images
        mock_get_title.return_value = mock_gallery_title
        mock_data = Mock()
        mock_obtain_document.return_value = mock_data
        gallery_processor = GalleryProcessor(mock_url, mock_credentials)

        assert gallery_processor.url == mock_url
        assert gallery_processor.credentials == mock_credentials
        assert not gallery_processor.random_pauses
        assert gallery_processor.image_index == 1
        assert gallery_processor.first_image_url == mock_first_image_url
        assert gallery_processor.total_number_images == mock_total_number_images
        assert gallery_processor.gallery_title == mock_gallery_title
        assert gallery_processor.folder_path == ''
        mock_obtain_document.assert_called_once_with(mock_url, mock_credentials)
        mock_get_first_image.assert_called_once_with(mock_data)
        mock_get_number_images.assert_called_once_with(mock_data)
        mock_get_title.assert_called_once_with(mock_data)

    @patch('exhentaidownloader.processor.gallery.obtain_document')
    @patch('exhentaidownloader.processor.gallery.get_gallery_title')
    @patch('exhentaidownloader.processor.gallery.get_number_of_images')
    def test_init_with_custom_path_and_title_with_pauses(self, mock_get_first_image, mock_get_number_images,
                                                         mock_obtain_document):
        mock_credentials = Credentials(Mock(), Mock())
        mock_url = 'mock_url'
        mock_first_image_url = 'mock_first_image_url'
        mock_total_number_images = 123
        mock_gallery_title = 'mock_gallery_title'
        mock_path = 'mock_path'
        mock_get_first_image.return_value = mock_first_image_url
        mock_get_number_images.return_value = mock_total_number_images
        mock_obtain_document.return_value = Mock()
        gallery_processor = GalleryProcessor(mock_url, mock_credentials, True, mock_path, mock_gallery_title)
        assert gallery_processor.random_pauses
        assert gallery_processor.gallery_title == mock_gallery_title
        assert gallery_processor.folder_path == mock_path

    @patch('exhentaidownloader.processor.gallery.obtain_document')
    @patch('exhentaidownloader.processor.gallery.get_number_of_images')
    @patch('exhentaidownloader.processor.gallery.get_first_image_page_link')
    def test_function_process_called_and_ok(self, mock_get_first_image, mock_get_number_images,
                                            mock_obtain_document):
        mock_credentials = Credentials(Mock(), Mock())
        mock_url = 'mock_url'
        mock_first_image_url = 'image_1'
        mock_total_number_images = 5
        mock_gallery_title = 'mock_gallery_title'
        mock_path = 'mock_path'
        mock_get_first_image.return_value = mock_first_image_url
        mock_get_number_images.return_value = mock_total_number_images
        mock_obtain_document.return_value = Mock()
        gallery_processor = GalleryProcessor(mock_url, mock_credentials, True, mock_path, mock_gallery_title)

        mock_images = ['image_2', 'image_3', 'image_4', 'image_5', 'image_5']
        expected_calls_get_image_link = []
        expected_calls_obtain_document = [call()]
        for x in range(1, 6):
            expected_calls_get_image_link.append(call(f'image_{x}'))
        gallery_processor.process()
        # TODO assert folder creation is called
        # TODO assert image save is called

    def test_function_sleep(self):
        start_time = time.time()
        GalleryProcessor.random_pause()
        end_time = time.time()
        time_1 = end_time - start_time

        start_time = time.time()
        GalleryProcessor.random_pause()
        end_time = time.time()
        time_2 = end_time - start_time

        assert time_1 != time_2

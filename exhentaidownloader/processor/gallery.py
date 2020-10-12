from random import randint
from time import sleep

from exhentaidownloader.web.connector import obtain_document
from exhentaidownloader.web.credentials import Credentials
from exhentaidownloader.web.scrapper import get_first_image_page_link, get_number_of_images, get_gallery_title, \
    get_image_link, get_next_image_page_link


class GalleryProcessor:
    def __init__(self, url: str = None, credentials: Credentials = None, random_pauses: bool = False,
                 folder_path: str = '', gallery_title: str = None):
        if url is None:
            raise Exception('Gallery url must be provided')
        if credentials is None:
            raise Exception('Credentials object must be provided')
        self.url = url
        self.credentials = credentials
        self.random_pauses = random_pauses
        self.image_index = 1

        data = obtain_document(url, credentials)
        self.first_image_url = get_first_image_page_link(data)
        self.total_number_images = get_number_of_images(data)
        self.folder_path = folder_path
        if gallery_title is None:
            self.gallery_title = get_gallery_title(data)
        else:
            self.gallery_title = gallery_title

    def process(self):
        #TODO call to create folder
        previous_image_page = ''
        current_image_page = self.first_image_url
        while previous_image_page != current_image_page:
            previous_image_page = current_image_page
            image_page_data = obtain_document(current_image_page, self.credentials)
            image_uri = get_image_link(image_page_data)
            #TODO Save image
            #TODO Log progress
            current_image_page = get_next_image_page_link(image_page_data)
            if self.random_pauses and previous_image_page != current_image_page:
                self.random_pause()


    @staticmethod
    def random_pause():
        sleep(randint(1, 10))

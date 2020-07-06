from exhentaidownloader.web import connector
from mock import patch
import requests


class TestConector:
    @patch('exhentaidownloader.web.connector.requests.request')
    def test_obtain_cookie_id_ok(self, mock_post):
        mock_member_id = 'mock_member_id'
        mock_pass_hash = 'mock_pass_hash'
        mock_user = 'mock_user'
        mock_pass = 'mock_pass'
        url = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"

        payload = {'CookieDate': '1',
                   'b': 'd',
                   'UserName': mock_user,
                   'PassWord': mock_pass,
                   'ipb_login_submit': 'Login!'}
        files = [

        ]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Origin': 'https://e-hentai.org',
            'Host': 'forums.e-hentai.org',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 '
                          '(KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': 'https://e-hentai.org/bounce_login.php',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        mock_response = requests.Response()
        mock_response.cookies.set('ipb_member_id', mock_member_id)
        mock_response.cookies.set('ipb_pass_hash', mock_pass_hash)
        mock_post.return_value = mock_response
        ipb_member_id, ipb_pass_hash = connector.obtain_credentials(mock_user, mock_pass)
        mock_post.assert_called_once_with("POST", url, headers=headers, data=payload, files=files)
        assert ipb_member_id == mock_member_id
        assert ipb_pass_hash == mock_pass_hash

    @patch('exhentaidownloader.web.connector.requests.request')
    def test_obtain_cookie_id_nok(self, mock_post):
        mock_user = 'mock_user'
        mock_pass = 'mock_pass'
        url = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"

        payload = {'CookieDate': '1',
                   'b': 'd',
                   'UserName': mock_user,
                   'PassWord': mock_pass,
                   'ipb_login_submit': 'Login!'}
        files = [

        ]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Origin': 'https://e-hentai.org',
            'Host': 'forums.e-hentai.org',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 '
                          '(KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Referer': 'https://e-hentai.org/bounce_login.php',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        mock_response = requests.Response()
        mock_post.return_value = mock_response
        ipb_member_id, ipb_pass_hash = connector.obtain_credentials(mock_user, mock_pass)
        mock_post.assert_called_once_with("POST", url, headers=headers, data=payload, files=files)
        assert ipb_member_id == None
        assert ipb_pass_hash == None

    def test_obtain_web_with_cookie_ok(self):
        pass

    def test_obtain_web_with_cookie_nok(self):
        pass
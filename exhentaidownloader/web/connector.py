import requests

from exhentaidownloader.web.credentials import Credentials


def obtain_credentials(user: str, password: str):
    url = "https://forums.e-hentai.org/index.php?act=Login&CODE=01"

    payload = {'CookieDate': '1',
               'b': 'd',
               'UserName': user,
               'PassWord': password,
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

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    cookies = response.cookies.get_dict()
    ipb_member_id = cookies.get('ipb_member_id')
    ipb_pass_hash = cookies.get('ipb_pass_hash')
    return Credentials(ipb_member_id, ipb_pass_hash)


def obtain_document(url: str, credentials: Credentials):
    headers = {
        'Cookie': f'ipb_member_id=1{credentials.ipb_member_id}; ipb_pass_hash={credentials.ipb_pass_hash}'
    }
    response = requests.request("GET", url, headers=headers)
    return response

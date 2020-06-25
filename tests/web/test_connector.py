from exhentaidownloader.web import connector
import pytest

class TestConector:
    def test_obtain_cookie_id_ok(self):
        ipb_member_id, ipb_pass_hash = connector.obtain_credentials('a', 'b')
        pass

    def test_obtain_cookie_id_nok(self):
        pass

    def test_obtain_web_with_cookie_ok(self):
        pass

    def test_obtain_web_with_cookie_nok(self):
        pass
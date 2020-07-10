from requests import Response


class MockResponse(Response):
    def __init__(self, content, status_code):
        super().__init__()
        self._content = content
        self.status_code = status_code

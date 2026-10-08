
from google_page import GooglePage


class TestGoogle:

    def test_google_search(self, page):

        google = GooglePage(page)

        google.open_google()
        google.search("Playwright Python")

        page.wait_for_load_state("networkidle")

        assert "Playwright" in google.get_title()

    def test_google_click(self, page):

        google = GooglePage(page)

        google.open_google()
        google.search("Microsoft")

        page.wait_for_timeout(6000)

        assert "Microsoft" in google.get_title()

    def test_google_hover(self, page):

        google = GooglePage(page)

        google.open_google()

        gmail = google.hover_gmail()

        assert gmail.is_visible()


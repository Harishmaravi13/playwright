class GooglePage:

    def __init__(self, page):
        self.page = page

    def open_google(self):
        self.page.goto("https://www.google.com")

    def search(self, text):
        self.page.fill("textarea[name='q']", text)
        self.page.press("textarea[name='q']", "Enter") 

    def hover_gmail(self):
        gmail = self.page.get_by_text("Gmail")
        gmail.hover()
        return gmail

    def get_title(self):
        return self.page.title()
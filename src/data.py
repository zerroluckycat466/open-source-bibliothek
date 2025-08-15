class Project:
    def __init__(self, name, description, language, url):
        self.name = name
        self.description = description
        self.language = language
        self.url = url

    def __str__(self):
        return f'{self.name} - {self.language}: {self.description}'
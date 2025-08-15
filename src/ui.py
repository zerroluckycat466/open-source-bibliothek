from src.database import Database

class UI:
    def __init__(self, db):
        self.db = db

    def show_projects(self):
        for project in self.db.projects:
            print(project)

    def add_project(self):
        name = input("Projektname: ")
        description = input("Projektbeschreibung: ")
        language = input("Programmiersprache: ")
        url = input("URL: ")
        new_project = Project(name, description, language, url)
        self.db.add_project(new_project)
        print(f'Projekt {name} wurde hinzugefügt!')
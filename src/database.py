import json
from src.data import Project

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.projects = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Project(**item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump([project.__dict__ for project in self.projects], file)

    def add_project(self, project):
        self.projects.append(project)
        self.save_data()
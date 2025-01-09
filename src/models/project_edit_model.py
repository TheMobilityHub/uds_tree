import yaml


class ProjectEditModel:
    def __init__(self):
        self.yml_data = {}
        self.file_path = None

    def load_yml(self, file_path):
        self.file_path = file_path
        with open(file_path, "r", encoding="utf-8") as file:
            self.yml_data = yaml.safe_load(file)

    def save_yml(self):
        if not self.file_path:
            raise ValueError("File path not set.")
        with open(self.file_path, "w", encoding="utf-8") as file:
            yaml.dump(self.yml_data, file)

    def update_yml(self, key, value):
        self.yml_data[key] = value

    def get_yml_data(self):
        return self.yml_data

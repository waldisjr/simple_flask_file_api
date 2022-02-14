from abc import ABC


class AbstractFileFuncs(ABC):
    def get_file_content(self) -> list:
        pass

    def add_content_to_file(self, new_content: str) -> None:
        pass

    def replace_file_content(self, new_content: str) -> None:
        pass

    def clear_file(self) -> None:
        pass


class FileFuncs(AbstractFileFuncs):
    def __init__(self, file_name):
        # check if the file exists
        try:
            open(file_name, "r")
        # if not - create a new one
        except FileNotFoundError:
            open(file_name, "w")

        self.file_name = file_name

    def get_file_content(self) -> list:
        with open(self.file_name, "r") as file:
            return file.readlines()

    def add_content_to_file(self, new_content: str) -> None:
        with open(self.file_name, "a") as file:
            file.write(new_content)

    def replace_file_content(self, new_content: str) -> None:
        with open(self.file_name, "w") as file:
            file.write(new_content)

    def clear_file(self) -> None:
        open(self.file_name, "w")

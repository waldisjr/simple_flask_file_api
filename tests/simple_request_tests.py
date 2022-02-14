import requests


class RequestsTest:
    def __init__(self, host):
        self.host = host

    def file_get(self):
        return requests.get(self.host+"file/").content

    def file_post(self, content):
        return requests.post(self.host + "file/", params={"new_content": content}).content

    def file_patch(self, content):
        return requests.patch(self.host + "file/", params={"new_content": content}).content

    def clear_file(self):
        return requests.delete(self.host + "file/").content


if __name__ == '__main__':
    test = RequestsTest("http://127.0.0.1:5000/")

    # print(test.file_post("test"))
    # print(test.file_patch("\nwertygvcd"))
    print(test.clear_file())

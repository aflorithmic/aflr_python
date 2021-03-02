import aflr
from aflr.api_request import APIRequest


class Mastering(APIRequest):
    OBJECT_NAME = "mastering"

    def __init__(self):
        super().__init__()
        self.file_url = self.api_base + "/file/mastering"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

	# get mastering file
    def retrieve(self, scriptId, parameters={}):
        parameters.update({'scriptId': scriptId})
        return self._get_request(url=self.file_url, request_params=parameters)

    # download mastering file
    def download(self, scriptId, parameters={}, destination="."):
        url = self.retrieve(scriptId=scriptId, parameters=parameters)
        url = url if type(url) == str else url.get('url')
        local_filename = self._download_request(url=url, destination=destination) 
        return local_filename

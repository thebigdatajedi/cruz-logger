from typing import Self, Any


class PreConfiguredS3BucketResource:

    def __init__(self):
        self._root_bucket_config: str = 's3://backup-regsvc-useast2/backup/ScrubbedDatabases/Gryphon/'

    @staticmethod
    def create() -> Any:
        # get the configured resource to be able to later access the pre-configured bucket
        configured_resource = PreConfiguredS3BucketResource()
        return configured_resource

    def get_config(self) -> str:
        return self._root_bucket_config

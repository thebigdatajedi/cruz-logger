- The difference between an instance variable and class in Python with example
- This class uses an instance variable to store the configuration string for the root bucket.  
- The instance is created with the create() static method that first creates a configured_resource object and then it 
- goes and then it has an instance get config method that is the getter for the root_bucket_config that just got instanciated. 
class PreConfiguredS3BucketResource:
   
    def __init__(self):
        self._root_bucket_config: str = 's3://backup-regsvc-useast2/backup/ScrubbedDatabases/Gryphon/'

    @staticmethod
    def create() -> str:
        # set the root bucket path
        configured_resource = PreConfiguredS3BucketResource()
        return configured_resource

    def get_config(self) -> str:
        return self._root_bucket_config
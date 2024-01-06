from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1007012assignment"
    account_key = "8WZFJKRqV+uay9RB3zBOqjy//+xwFJLct0KGYMUP217EJmrUsvMq/C+WC/0qALBpG1OLY7WI2gjQ+AStbjnROQ=="
    azure_container = "media"
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "c1007012assignment"
    account_key = "8WZFJKRqV+uay9RB3zBOqjy//+xwFJLct0KGYMUP217EJmrUsvMq/C+WC/0qALBpG1OLY7WI2gjQ+AStbjnROQ=="
    azure_container = "static"
    expiration_secs = None
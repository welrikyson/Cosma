from src.utils.file_storage import FileStore

filename = "globals.pickle"


class Globals:

    @staticmethod
    def set_last_activity_date_notify(last_date):
        FileStore.save(last_date, filename)

    @staticmethod
    def get_last_activity_date_notify():
        return FileStore.load(filename)





from ko.ko import Ko

class ExtendedKo(Ko):
    def __init__(self):
        super().__init__()

    def show_version(self):
        version = self.get_version()
        print(f"The version of this app is: {version}")
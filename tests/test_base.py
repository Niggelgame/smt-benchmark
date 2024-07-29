from environment import environment


class TestBase:
    def get_info(self):
        pass

    def run_test(self):
        pass


    def log(self, msg, lvl):
        name = self.get_info()["name"]

        if lvl <= environment["LOG_LEVEL"]:
            print(f"[{name}] {msg}")
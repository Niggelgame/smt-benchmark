from environment import environment


class TestBase:
    def get_info(self):
        """
        Return the information about the test suite.

        Must specify:
        - name: str (name of the test suite)
        - required_environment: array of str (environment variables required for the test)
        
        can specify:
        - description: str (description of the test suite)
        - enabled: bool (whether the test suite is enabled)
        """
        pass

    def run_test(self):
        """
        Run the test suite. 

        Must return a dictionary of results.
        """

        pass


    def log(self, msg, lvl):
        """
        Log a message with a specific level. (specified by environment["LOG_LEVEL"])
        """
        name = self.get_info()["name"]

        if lvl <= environment["LOG_LEVEL"]:
            print(f"[{name}] {msg}")
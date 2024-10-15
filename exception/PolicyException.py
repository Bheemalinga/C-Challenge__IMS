class PolicyNotFoundException(Exception):
    def __init__(self):
        Exception.__init__(self, "No such policy exists")

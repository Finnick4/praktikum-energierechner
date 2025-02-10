class BadResponse(Exception):
    def __init__(self, rc):
        super().__init__(f"Got a bad response! Should be 200, but got {rc}")

class DiffrentUnit(Exception):
    def __init__(self):
        super().__init__("Got a diffrent Unit than expected!")

    def __init__(self, gotten):
        # gotten -> Unit you got
        super().__init__(f"Got a diffrent Unit than expected! Got: {gotten}")

    def __init__(self, gotten, required):
        super().__init__(f"Got a diffrent Unit than expected! Got: {gotten} instead of {required}")
    
    def __init__(self, required):
        super().__init__(f"Got a diffrent Unit than expected! The program wants: {required}")

class ContentNotAvailable(Exception):
    def __init__(self):
        super().__init__("The wanted content is not available!")

class DiffrentTimestamp(Exception):
    def __init__(self, ts):
        super().__init__(f"Got a diffrent timestamp back: {ts}")
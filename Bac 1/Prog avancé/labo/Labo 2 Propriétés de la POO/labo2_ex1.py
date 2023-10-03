class ExempleClass:
    a = 1
    def __init__(self):
        self.b = 2
exemple_object = ExempleClass()
print(hasattr(exemple_object,'b'))
print(hasattr(exemple_object,'a'))
print(hasattr(ExempleClass,'b'))
print(hasattr(ExempleClass,'a'))
class Bavul:
    kutle:int

    def __init__(self,kutle:int = 5):
        self.kutle=kutle

    def __repr__(self):
        text  = str(self.kutle)+" ağırlığında bavul"
        return text
        
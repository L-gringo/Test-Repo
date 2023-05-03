from abc import ABC
#class qui définit un fichier
class file(ABC):
    def __init__(self,title,size):
        self.title=title
        self.size=size
    
    def add():
        pass
    def display():
        pass

#classe enfant de la classe fichier qui définit un fichier de type PNG
class filePNG(file):
    def __init__(self,title,size,type="PNG"):
        super().__init__(title,size)
        self.type=type
    def add():
        pass
    def display():
        pass
#classe enfant de la classe fichier qui définit un fichier de type JPEG
class fileJPEG(file):
    def __init__(self,title,size,type="JPEG"):
        super().__init__(title,size)
        self.type=type
    def add():
        pass
    def display():
        pass
#classe enfant de la classe fichier qui définit un fichier de type FLV
class filevideo(file):
    def __init__(self,title,size,type="flv"):
        super().__init__(title,size)
        self.type=type
    def add():
        pass
    def display():
        pass

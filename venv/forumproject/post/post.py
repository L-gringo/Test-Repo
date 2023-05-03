#class qui définit un post
class Post:
    def __init__(self,content,publishdate,publisher):
        self.content=content
        self.publishdate=publishdate
        self.publisher=publisher
    
    def display(self):
        print(f"message Publié par {self.publisher.username} le {self.publishdate}:")
        print(f" {self.content}")
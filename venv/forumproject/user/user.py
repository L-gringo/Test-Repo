#class qui définit un utilisateur
class user:
    def __init__(self,login,password,username):
        self.login=login
        self.password=password
        self.username=username
    
#class qui définit un utilisateur
class user:
    def __init__(self,login,password,username):
        self.login=login
        self.password=password
        self.username=username
    
    def addpostmessage(self,listposts,thread,post):
        #thread.addpost(listposts,post.content)
        thread.addpost(listposts,post)

class moderator(user):
    def __init__(self,login,password,username):
        super().__init__(login,password,username)
    
    def modifypost(self,thread,oldpost,newpost,listposts):
        thread.modif(listposts,oldpost,newpost)

    def deletepost(self,listposts,thread,Post):
        thread.delete(listposts,Post) 

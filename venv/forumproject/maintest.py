from abc import ABC


#classe qui définit un thread
class thread:
    
    def __init__(self,title,maker,createdate):
        self.title=title
        self.maker=maker
        self.createdate=createdate
        
    def addpost(self,listposts,post):
        #print(post.content)
        listposts.append(post)
    
    def addimagefile(self, listposts,file):
        listposts.append(file.title)

    def delete(self,listposts,post):
        #listposts.remove(post.content)
        listposts.remove(post)
    
    def modif(self,listposts,oldpost,newpost):
        #index=listposts.index(oldpost.content)
        #listposts[index]=newpost
        index=listposts.index(oldpost)
        listposts[index].content=newpost
    
    def display(self,listposts):
        print(f"-----Thread créé par {self.maker.username}-----")
        print(f"---------{self.title}--------------")
        for post in listposts:
            post.display()
            #print(post)
            print("------------------")
           # print(post)

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

#class qui définit un post
class Post:
    def __init__(self,content,publishdate,publisher):
        self.content=content
        self.publishdate=publishdate
        self.publisher=publisher
    
    def display(self):
        print(f"message Publié par {self.publisher.username} le {self.publishdate}:")
        print(f" {self.content}")

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

#méthodes permettant de faire des actions sur des fichiers
def addimagefile(thread,listposts,file,user):
        
        if file.type=="PNG":
            print(f"fichier PNG de {file.size} uploadé par {user.username}")
            print(f"{file.title}")
            thread.addimagefile(listposts,file)
        
        if file.type=="JPEG":
            print(f"fichier JPEG de {file.size} uploadé par {user.username}")
            print(f"{file.title}")
            thread.addimagefile(listposts,file)

def addvideos(thread,listposts,file,user):
            print(f"fichier vidéo de {file.size} uploadé par {user.username}")
            print(f"{file.title}")
            thread.addimagefile(listposts,file)


def main():
    #liste qui instancie la liste des posts publiés dans un thread
    listposts=[]
    user1=user("gringo",123,"lgringo")
    moderator1=moderator("maddog",1234,"wafwaf")
    thread1=thread("Python",user1,"aujourd'hui")
    post1=Post("python c'est quand même chouette","Aujourd'hui",user1)
    user1.addpostmessage(listposts,thread1,post1)
    postmod=Post("Ouais je suis d'accord","Aujourd'hui",moderator1)
    moderator1.addpostmessage(listposts,thread1,postmod)
    post1=Post("En même temps j'adore les ulcs","Aujourd'hui",user1)
    user1.addpostmessage(listposts,thread1,post1)
    postmod=Post("Mmm bruh, c'est pas halal ca ici","Aujourd'hui",moderator1)
    moderator1.addpostmessage(listposts,thread1,postmod)
    moderator1.deletepost(listposts,thread1,post1)
    post1=Post("Ahh sorry mista","Aujourd'hui",user1)
    user1.addpostmessage(listposts,thread1,post1)
    moderator1.modifypost(thread1,post1,"ahh sorry mister",listposts)
    thread1.display(listposts)
    file1=filePNG("apologize","15mo")
    addimagefile(thread1,listposts,file1,user1)
    
main()
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

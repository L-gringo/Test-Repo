from forumproject.file.file import filePNG
from forumproject.fileactions.fileactions import addimagefile
from forumproject.post.post import Post
from forumproject.user.user import user,moderator
from forumproject.thread.thread import thread

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

if __name__=="__main__":
        main()
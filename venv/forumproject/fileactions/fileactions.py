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

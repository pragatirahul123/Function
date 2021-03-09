def student(*name):
    index=0
    new=[]
    while index<len(name):
        new.append(name[index])
        index=index+1
    print(new)
        
student("mona","hina","sona","rina","teena")



# comment isminde bir class oluşturun
# comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdır

class Comment:
    def __init__(self,username,text,likes=0,dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment("semih","Yorumum iyi")
c2 = Comment("ali","Yorumum çok iyi",10,5)
c3 = Comment("erkan","Yorumum kötü",5,68)
c4 = Comment("serkan","Yorumum idare eder",10,15)
c5 = Comment("mehmet","Yorumum mükemmel",100,5)

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"Likes: {c.likes} Dislikes: {c.dislikes}")

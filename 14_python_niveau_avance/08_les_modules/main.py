# import blog
from blog import Article, Auteur


article = Article("Premier article", "Le contenu de mon article")
article.afficher()

auteur = Auteur("Emile", "Zola")
auteur.info()
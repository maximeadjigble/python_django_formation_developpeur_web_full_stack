from blog.article import Article
from blog.utilisateur import Auteur

article = Article("Premier article", "Le contenu de mon article")
article.afficher()

auteur = Auteur("Emile", "Zola")
auteur.info()
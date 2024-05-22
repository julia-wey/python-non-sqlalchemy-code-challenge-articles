class Article:

    all = []

    def __init__(self, author, magazine, title):
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.add_new_article(self)

    @classmethod
    def add_new_article(cls, new_article):
        cls.all.append(new_article)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, '_title'):
            self._title = new_title
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine 

class Author:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name') and isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(magazine=magazine, author=self, title=title)

    def topic_areas(self):
        if self.articles():
            return list(set(article.magazine.category for article in self.articles()))
        else:
            return None 

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        if self.articles():
            return [article.title for article in self.articles()]
        else:
            return None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if isinstance(article.author, Author):
                author_count[article.author] = author_count.get(article.author, 0) +1
        return [author for author, count in author_count.items() if count > 2] or None
        
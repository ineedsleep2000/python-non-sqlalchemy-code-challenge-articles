#####################################
#Article class 
class Article:

    all=[]

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)
    #####################################
    #Article title property (Initializers and Properties)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <=50 and not hasattr(self, "title"):
            self._title = title
        else:
            raise TypeError

    ##################################### 
    #Article author property (Object Relationship Methods and Properties)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    #####################################
    #Article magazine property (Object Relationship Methods and Properties)

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine

    #####################################
#####################################





#####################################
#Author class       
class Author:

    all=[]

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    #####################################
    #Author name property (Initializers and Properties)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) and not hasattr(self, "name"):
            self._name = name
        else:
            raise ValueError

    #####################################     
    #Author articles() (Object Relationship Methods and Properties)

    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    #####################################
    #Author magazines() (Object Relationship Methods and Properties)

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    #####################################
    #Author add_article() (Aggregate and Association Methods)

    def add_article(self, magazine, title):
        added_articles= Article(self, magazine, title)
        return added_articles

    #####################################  
    #Author topic_areas() (Aggregate and Association Methods) 

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    #####################################
#####################################





#####################################
#Magazine class
class Magazine:

    all=[]

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    #####################################
    #Magazine name property (Initializers and Properties)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError

    #####################################   
    #Magazine category property (Initializers and Properties)

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str):
            self._category = category
        else:
            raise TypeError 
        if 1 <= len(category):
            self._category = category
        else:
            raise ValueError
            

    #####################################  
    #Magazine articles() (Object Relationship Methods and Properties)

    def articles(self):
        return [articles for articles in Article.all if articles.magazine == self]

    #####################################
    #Magazine contributors() (Object Relationship Methods and Properties)

    def contributors(self):
        return list(set([articles.author for articles in self.articles()]))

    #####################################
    #Magazine article_titles() (Aggregate and Association Methods)
    
    def article_titles(self):
        titles = [articles.title for articles in self.articles()]
        if titles:
            return titles
        else:
            return None

    #####################################
    #Magazine contributing_authors() (Aggregate and Association Methods)
   
    def contributing_authors(self):
        authors = {}
        list_of_authors = []

        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        if (list_of_authors):
            return list_of_authors
        else:
            return None
            
    #####################################
#####################################
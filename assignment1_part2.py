class Book(object):
   
    author = ''
    title = ''
    
    def __init__(self, title, author):

        self.title = title
        self.author = author
        

        
    def display(self):
               
        print "{}, written by {}".format(self.title, self.author)
        
book1 = Book('Of Mice and Men','John Steinbeck')
book2 = Book('To Kill A Mockingbird','Harper Lee')

book1.display()
book2.display()

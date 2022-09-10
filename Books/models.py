from django.db import models


class Book_Category(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.Category_name

class Books_Model(models.Model):
    book_name = models.CharField(max_length=20)
    books_author = models.CharField(max_length=20)
    books_category = models.ForeignKey(Book_Category,on_delete=models.CASCADE,related_name="category")
    books_quantity = models.IntegerField()  

    def __str__(self)-> str:
        return self.book_name

from django.db import models

# Create your models here.
from django.urls import reverse # To generate URLS by reversing URL patterns


class Genre(models.Model):
	"""Model representing a book genre."""
	name = models.CharField(max_length=200, 
		help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=200)

	author = models.ForeignKey('Author', 
		on_delete=models.SET_NULL, null=True)

	summary = models.TextField(max_length=1000, 
		help_text='Enter a brief description of the book')

	isbn = models.CharField('ISBN', 
		max_length=13, help_text='13 Character ISBN number')

	genre = models.ManyToManyField(Genre, 
		help_text='Select a genre for this book')

	def __str__(self):
		"""String for representing the Model object."""
		return self.title
		
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
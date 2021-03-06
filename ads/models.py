from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.urlresolvers import reverse

from djmoney.models.fields import MoneyField

from users.models import User
from categories.models import Category
from locations.models import Location


class Ad(models.Model):
    # TODO: Add a set of images.
    # TODO: Add view count.
    title        = models.CharField(max_length=120)
    description  = models.TextField(validators=[MinLengthValidator(60),])
    author       = models.ForeignKey(User)
    location     = models.ForeignKey(Location, blank=True, null=True)
    categories   = models.ManyToManyField(Category)
    image        = models.ImageField(upload_to='img', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    price        = MoneyField(max_digits=10, decimal_places=2,
                   default_currency='RUB', validators=[MinValueValidator(0.01)])

    def get_absolute_url(self):
        return reverse('ads:show', args=(self.id,))

    def is_author(self, user):
        return user.id == self.author.id

    def __str__(self):
        return self.title

from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
from versatileimagefield.fields import VersatileImageField
from django_prices.models import MoneyField
from django.conf import settings


class Category(TranslatableModel):

    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True, unique=True)
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(TranslatableModel):

    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        description = models.TextField(blank=True)
    )

    image = VersatileImageField(upload_to='products/%Y/%m/%d', blank=True)
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    price = MoneyField(currency=settings.DEFAULT_CURRENCY, max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
from django.db import models
from django.contrib.auth.models import User


# ------Создание модели товаров------
class Product(models.Model):

	# Категории товаров
	t_shirt = "футболки"
	hoody = "кофты"
	other = "другое"
	CATEGORY = (
		(t_shirt,"футболки"),
		(hoody, "кофты"),
		(other, "другое")
		)


	name = models.CharField(max_length=200, db_index=True) # Имя
	category = models.CharField(max_length=9,choices=CATEGORY,default=other)
	image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # Картинка
	description = models.TextField(blank=True) # Описание
	price = models.DecimalField(max_digits=10, decimal_places=2) # цена
	stock = models.PositiveIntegerField() # Сколько осталось
	available = models.BooleanField(default=True) # есть ли товар
	created = models.DateTimeField(auto_now_add=True) # дата создания
	updated = models.DateTimeField(auto_now=True) # дата обновления

	def __str__(self):
		return self.name

class CartProduct(models.Model):

	s = 'S'
	m = 'M'
	l = 'L'
	SIZE = (
		(s,"S"),
		(m,"M"),
		(l,"L")
		)


	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	count = models.PositiveIntegerField(default=1)
	size = models.CharField(max_length=10, choices=SIZE,default=m)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)



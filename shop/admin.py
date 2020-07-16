from django.contrib import admin
from django.db import models
from django.urls import reverse

from .models import (
	Product, OrderItem, Order,
	Address, Payment, Refund, Category
)



def make_refund_accepted(modeladmin, request, queryset):
	queryset.update(refund_request=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = [
			'name', 
			'slug', 
			'price',
			'available', 
			'created', 
			'updated'
	]
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}


class OrderAdmin(admin.ModelAdmin):
	list_display = [
			'user', 
			'ordered', 
			'being_delivered',
			'received',
			'refund_request',
			'refund_granted',
			'billing_address',
			'shipping_address',  
			'payment',
	]
	list_filter = [
			'user', 
			'ordered', 
			'being_delivered',
			'received',
			'refund_request',
			'refund_granted'
	]
	list_display_links = [
			'user', 
			'billing_address',
			'shipping_address',    
			'payment',
	]
	search_fields = [
		'user__username',
		'ref_code',
	]
	actions = [make_refund_accepted]

class AddressAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'street_address',
		'apartment_address',
		'country',
		'zip_code',
		#'address_type',
		'default',
	]
	list_filter = [
		'default',
		#'address_type',
		'country',
	]
	search_fields = [
		'user',
		'street_address',
		'apartment_address',
		'zip_code',
	]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
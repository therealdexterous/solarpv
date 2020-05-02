# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
	Model_Number = models.CharField(max_length=50, null=True)
	Product_Name = models.CharField(max_length=50, null=True)
	Cell_Technology = models.CharField(max_length=50, null=True)
	Cell_Manufacturer = models.CharField(max_length=50, null=True)
	Number_of_Cells = models.CharField(max_length=50, null=True)
	Number_of_Cells_in_Series = models.CharField(max_length=50, null=True)
	Number_of_Series_in_Strings = models.CharField(max_length=50, null=True)
	Number_of_Diodes = models.CharField(max_length=50, null=True)
	Product_Length = models.CharField(max_length=50, null=True)
	Product_Width = models.CharField(max_length=50, null=True)
	Product_Weight = models.CharField(max_length=50, null=True)
	Superstate_Type = models.CharField(max_length=50, null=True)
	Superstate_Manufacturer = models.CharField(max_length=50, null=True)
	Substrate_Type = models.CharField(max_length=50, null=True)
	Substrate_Manufacturer = models.CharField(max_length=50, null=True)
	Frame_Type = models.CharField(max_length=50, null=True)
	Frame_Adhesive = models.CharField(max_length=50, null=True)
	Encapsulate_Type = models.CharField(max_length=50, null=True)
	Encapsulant_Manufacturer = models.CharField(max_length=50, null=True)
	Junction_Box_Type = models.CharField(max_length=50, null=True)
	Junction_Box_Manufacturer = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Product_Name

class Certificate(models.Model):
	Certificate_Number = models.CharField(max_length=50, null=True)
	User_ID = models.CharField(max_length=50, null=True)
	Report_Number = models.CharField(max_length=50, null=True)
	Issue_Date = models.DateField()
	Standard_ID = models.CharField(max_length=50, null=True)
	Location_ID = models.CharField(max_length=50, null=True)
	Model_Number = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.Certificate_Number

class Service(models.Model):
	Service_ID = models.CharField(max_length=50, null=True)
	Service_Name = models.CharField(max_length=50, null=True)
	Description = models.CharField(max_length=50, null=True)
	Is_FI_Required = models.CharField(max_length=50, null=True)
	FI_Frequency = models.CharField(max_length=50, null=True)
	Standard_ID = models.ForeignKey(Certificate, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.Service_Name

class Registered_Company(models.Model):
	name = models.CharField(max_length=100, null=True)
	clientID = models.CharField(max_length=50,null=True, unique=True)

	def __str__(self):
		return self.name

class Registered_User(models.Model):
	PREFIX = (
		('Dr.', 'Dr.'),
		('Mr.', 'Mr.'),
		('Ms.', 'Ms.'),
		('Mrs.', 'Mrs.'),
		)
	userID = models.CharField(max_length=50, null=False, unique=True)
	password = models.CharField(max_length=50, null=False, default="")
	clientID = models.CharField(max_length=50, null=True)
	first_name = models.CharField(max_length=50, null=False, default="")
	middle_name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=False, default="")
	job_title = models.CharField(max_length=50, null=True)
	email_address = models.CharField(max_length=50, null=True)
	office_phone = models.CharField(max_length=50, null=True)
	cell_phone = models.CharField(max_length=50, null=True)
	prefix = models.CharField(max_length=50, null=True, choices=PREFIX)

	def __str__(self):
		return self.userID

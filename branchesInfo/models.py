from __future__ import unicode_literals

from django.db import models
# Create your models here.

class BaseModel(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date_edited = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Break(BaseModel):
	time_from = models.CharField(max_length=50)
	time_to = models.CharField(max_length=50)
	isWithoutBreak = models.BooleanField(default=False)


class Currency(BaseModel):
	code = models.CharField(max_length=10)
	description = models.CharField(max_length=255)


class Service(BaseModel):
	name = models.CharField(max_length=255)


class Schedule(BaseModel):
	DAY_KEYS = (MON, TUE, WED, THU, FRI, SAT, SUN) = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')
	DAY_CAPS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
	DAY_OPTIONS = zip(DAY_KEYS, DAY_CAPS)

	day = models.CharField(max_length=10, choices=DAY_OPTIONS)
	time_from = models.CharField(max_length=50, null=True)
	time_to = models.CharField(max_length=50, null=True)
	isDayOff = models.BooleanField(default=False)


class BranchManager(models.Manager):

	def create_branch(self, **data):
		branche = Branch.objects.create(**data)
		return branche

	def update_branch(self, instance, **data):
		return instance


class Branch(BaseModel):
	TYPE_KEYS = (BRANCH, ATM, ATM24, TEMINAL) = ('BRANCH', 'ATM', 'ATM24', 'TERMINAL')
	TYPE_CAPS = ('Branch', 'Atm', 'Atm24', 'Terminal')
	TYPE_OPTIONS = zip(TYPE_KEYS, TYPE_CAPS)

	CLIENT_KEYS = (INDIVIDUAL, CORPORATION, BOTH) = ('INDIVIDUAL', 'CORPORATION', 'BOTH')
	CLIENT_CAPS = ('Individual', 'Corporation', 'Individual/Corporation')
	CLIENT_OPTIONS = zip(CLIENT_KEYS, CLIENT_CAPS)

	ACCESS_KEYS = (LIMITED, UNLIMITED) = ('LIMITED', 'UNLIMITED')
	ACCESS_CAPS = ('Limited entrance', 'Unlimited entance')
	ACCESS_OPTIONS = zip(ACCESS_KEYS, ACCESS_CAPS)


	isActive = models.BooleanField(default=True)
	type = models.CharField(max_length=10, choices=TYPE_OPTIONS, default=BRANCH)
	isCashIn = models.BooleanField(default=False)
	lat = models.DecimalField(max_digits=15, decimal_places=6, null=True)
	lng = models.DecimalField(max_digits=15, decimal_places=6, null=True)
	branchNumber = models.IntegerField(null=True)
	city = models.CharField(max_length=1024)
	name = models.CharField(max_length=1024)
	address = models.CharField(max_length=1024)
	clients = models.CharField(max_length=10, choices=CLIENT_OPTIONS, default=INDIVIDUAL)
	access = models.CharField(max_length=10, choices=ACCESS_OPTIONS, default=UNLIMITED)
	branchBreak = models.ForeignKey(Break, related_name="branches")
	currencies = models.ManyToManyField(Currency, related_name="branches")
	services = models.ManyToManyField(Service, related_name="branches")
	schedule = models.ManyToManyField(Schedule, related_name="branches")

	objects = BranchManager()




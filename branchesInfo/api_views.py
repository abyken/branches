from rest_framework import viewsets, response, filters, status
from rest_framework.decorators import list_route, detail_route
from branchesInfo.models import *
from branchesInfo.serializers import *

class BranchViewSet(viewsets.ModelViewSet):
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer

	
class BreakViewSet(viewsets.ModelViewSet):
	queryset = Break.objects.all()
	serializer_class = BreakSerializer

	
class CurrencyViewSet(viewsets.ModelViewSet):
	queryset = Currency.objects.all()
	serializer_class = CurrencySerializer

	
class ServiceViewSet(viewsets.ModelViewSet):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	
class ScheduleViewSet(viewsets.ModelViewSet):
	queryset = Schedule.objects.all()
	serializer_class = ScheduleSerializer

	

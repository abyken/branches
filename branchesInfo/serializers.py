from rest_framework import serializers
from .models import *

__all__ = (
	'BreakSerializer',
	'CurrencySerializer',
	'ServiceSerializer',
	'ScheduleSerializer',
	'BranchSerializer'
)

class BreakSerializer(serializers.Serializer):

	class Meta:
		model = Break


class CurrencySerializer(serializers.Serializer):

	class Meta:
		model = Currency


class ServiceSerializer(serializers.Serializer):

	class Meta:
		model = Service


class ScheduleSerializer(serializers.Serializer):

	class Meta:
		model = Schedule


class BranchSerializer(serializers.Serializer):

	class Meta:
		model = Branch

	branchBreak = BreakSerializer(required=False)
	currencies = CurrencySerializer(required=False, many=True)
	services = ServiceSerializer(required=False, many=True)
	schedule = ScheduleSerializer(required=False, many=True)

	def create(self, validated_data):
		return Branch.objects.create_branch(**validated_data)

	def update(self, instance, validated_data):
		return Branch.objects.update_branch(**validated_data)

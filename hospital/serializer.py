from rest_framework import serializers
from .models import patient
from .models import hosp

class patient_serializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = [ 'p_id', 'name', 'room', 'hospital', 'disease', 'status', 'allergies', 'remarks']

  
class hosp_serializer(serializers.ModelSerializer):
    single = serializers.IntegerField(default=1)
    double = serializers.IntegerField(default=1)
    triple = serializers.IntegerField(default=1)

    class Meta:
        model = hosp
        fields = ['r_id', 'single', 'double', 'triple']

# class del_bed_serializer(serializers.Serializer):
#     r_id = serializers.IntegerField(default=1)
#     class Meta:
#         fields = ['r_id']
'''
class hosp_serializer(serializers.Serializer):
    # r_id = serializers.AutoField()
    single = serializers.IntegerField(default=1)
    double = serializers.IntegerField(default=1)
    triple = serializers.IntegerField(default=1)
    # created = serializers.DateTimeField()
'''
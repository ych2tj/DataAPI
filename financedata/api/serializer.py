from rest_framework import serializers
from ..models import shareprice

class sharepriceSerial(serializers.ModelSerializer):
    created = serializers.SerializerMethodField()
    class Meta:
        model = shareprice
        fields = (
            'id',
            'date',
            'open',
            'high',
            'low',
            'close',
            'volumn',
            'change',
            'changePercent',
            'symbol',
            'created'
        )
        
    def get_created(self, obj):
        return obj.created.strftime('%Y-%m-%d %H:%M:%S')

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MedicalCardSerializer, RecordSerializer
from .models import MedicalCard, Record


@api_view(['GET'])
def medical_card_info(request, pk):
    medical_card = MedicalCard.objects.get(number=pk)
    serializer = MedicalCardSerializer(medical_card, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def medical_card_records(request, pk):
    records = Record.objects.filter(medical_card=pk)
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from .models import SaidLemma
from .serializes import SentenceTextSerializer
import environ
import logging

logger = logging.getLogger(__name__)

# TODO set minimum confidence level with feature toggle
minimum_confidence = 0.0


@api_view(['POST'])
@parser_classes([JSONParser])
def sentence(request):
    serializer = SentenceTextSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        vosk_final_result = request.data
        for partial_results in vosk_final_result['result']:
            if minimum_confidence <= partial_results['conf']:
                lem = SaidLemma(
                    word_lemma=partial_results['word'],
                    date_said=timezone.now(),
                )
                lem.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


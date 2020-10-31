from django.utils import timezone
from rest_framework.response import Response
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
    try:
        print(serializer.is_valid())
        print(serializer.errors)
    except Exception as ex:
        print(ex)
    if serializer.is_valid():
        try:
            vosk_final_result = request.data
            if environ('DEBUG'):
                print(vosk_final_result)
            for partial_results in vosk_final_result['result']:
                if minimum_confidence <= partial_results['conf']:
                    lem = SaidLemma(
                        word_lemma=partial_results['word'],
                        date_said=timezone.now(),
                    )
                    lem.save()
        except Exception as ex:
            logger.error(ex)
    return Response({'received data': request.data})

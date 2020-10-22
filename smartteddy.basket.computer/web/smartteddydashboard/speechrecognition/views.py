from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from .models import LemmaCounter

# TODO set minimum confidence level with feature toggle
minimum_confidence = 0.0


@api_view(['POST'])
@parser_classes([JSONParser])
def sentence(request):
    try:
        vosk_final_result = request.data
        print(vosk_final_result)
        for partial_results in vosk_final_result['result']:
            if minimum_confidence <= partial_results['conf']:
                lem = LemmaCounter(
                    word_lemma=partial_results['word'],
                    date_said=timezone.now(),
                )
                lem.save()
    except Exception as ex:
        print(ex)
    return Response({'received data': request.data})

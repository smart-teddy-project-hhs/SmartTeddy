from django.db import models
from django.utils import timezone
import datetime

POSITIVE = 'POS'
NEGATIVE = 'NEG'
SENTIMENT_POLARITY_CHOICES = [
    (POSITIVE, 'positive'),
    (NEGATIVE, 'negative'),
]

ADJECTIVE = 'ADJE'
NOUN = 'NOUN'
VERB = 'VERB'
OTHER = 'OTHE'
PART_OF_SPEECH_CHOICES = [
    (ADJECTIVE, 'adjective'),
    (NOUN, 'noun'),
    (VERB, 'verb'),
    (OTHER, 'other'),
]


class SentimentLemma(models.Model):

    lemma_written_form = models.CharField(max_length=100)
    sense_confidence_level = models.CharField(max_length=100)
    sentiment_polarity = models.CharField(
        max_length=3,
        choices=SENTIMENT_POLARITY_CHOICES,
        default=NEGATIVE
    )
    part_of_speech = models.CharField(
        max_length=4,
        choices=PART_OF_SPEECH_CHOICES,
        default=OTHER
    )

    def __str__(self):
        return f'{self.lemma_written_form} has a {self.sentiment_polarity} sentiment'


class LemmaCounter(models.Model):
    # TODO create link (foreign key) for filtering a group of sentiment lemma's and recognized lemma's.
    word_lemma = models.CharField(max_length=100, default='<ukn>')
    date_said = models.DateTimeField('Date said on')

    def was_said_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_said <= now
    was_said_recently.boolean = True
    was_said_recently.admin_order_field = 'date_said'
    was_said_recently.short_description = 'Said last week'

    def __dir__(self):
        return f'{self.sentiment_lemma} is said on {self.date_said}'
from django.db import models
from django.utils import timezone
import datetime
from datetime import date

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

    @property
    def is_positive(self):
        return True if self.sentiment_polarity == POSITIVE else False

    def __str__(self):
        # TODO add to admin instead of __str__ method
        # return f'{self.lemma_written_form} has a {self.sentiment_polarity} sentiment'
        return self.sentiment_polarity


class SaidLemma(models.Model):
    id = models.BigAutoField(primary_key=True)
    word_lemma = models.CharField(max_length=100, default='<ukn>')
    date_said = models.DateTimeField('Date said on')
    week_number_said = models.PositiveSmallIntegerField(
        default=int(date.today().isocalendar()[1]),
    )
    sentiment = models.ForeignKey(
        SentimentLemma,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def was_said_last_week(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.date_said <= now

    was_said_last_week.boolean = True
    was_said_last_week.admin_order_field = 'date_said'
    was_said_last_week.short_description = 'Said last week'

    def save(self, *args, **kwargs):
        # TODO find a less heuristic for sentiment
        search_sentiment = SentimentLemma.objects.filter(lemma_written_form=self.word_lemma)
        if search_sentiment.count() == 1:
            print(search_sentiment[0])
            self.sentiment = search_sentiment[0]
        self.week_number_said = int(self.date_said.isocalendar()[1])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.word_lemma} is said on {self.date_said.strftime('%Y-%m-%d %H:%M')}"

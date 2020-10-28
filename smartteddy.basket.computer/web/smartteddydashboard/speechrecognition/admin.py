from django.contrib import admin
from .models import SentimentLemma, SaidLemma


class SentimentLemmaAdmin(admin.ModelAdmin):
    model = SentimentLemma
    fieldsets = [
        (None, {'fields': ['lemma_written_form', 'sentiment_polarity', 'part_of_speech']}),
    ]
    list_display = ('lemma_written_form', 'sentiment_polarity', 'part_of_speech')
    search_fields = ['lemma_written_form', 'sentiment_polarity', 'part_of_speech']
    list_filter = ['sentiment_polarity', 'part_of_speech']


admin.site.register(SentimentLemma, SentimentLemmaAdmin)


class SaidLemmaAdmin(admin.ModelAdmin):
    model = SaidLemma
    fieldsets = [
        (None, {'fields': ['word_lemma', 'date_said']}),
    ]
    list_display = ('word_lemma', 'date_said', 'week_number_said', 'sentiment')
    search_fields = ['word_lemma']
    list_filter = ['date_said']
    orderning = ['-date_said']


admin.site.register(SaidLemma, SaidLemmaAdmin)

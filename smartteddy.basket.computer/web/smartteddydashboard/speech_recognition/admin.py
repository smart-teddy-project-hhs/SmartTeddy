from django.contrib import admin

from .models import SentimentLemma


class SentimentLemmaInline(admin.TabularInline):
    model = SentimentLemma


class SentimentLemmaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['lemma_written_form', 'sentiment_polarity', 'part_of_speech']}),
    ]
    list_display = ('lemma_written_form', 'sentiment_polarity', 'part_of_speech')
    search_fields = ['lemma_written_form', 'sentiment_polarity', 'part_of_speech']
    list_filter = ['sentiment_polarity', 'part_of_speech']


admin.site.register(SentimentLemma, SentimentLemmaAdmin)

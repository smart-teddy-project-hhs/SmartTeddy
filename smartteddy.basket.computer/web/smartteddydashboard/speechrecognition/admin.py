from django.contrib import admin

from .models import SentimentLemma, LemmaCounter


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


class LemmaCounterInline(admin.TabularInline):
    model = LemmaCounter


class LemmaCounterAdmin(admin.ModelAdmin):
    model = LemmaCounter
    fieldsets = [
        (None, {'fields': ['word_lemma', 'date_said', 'week_number_said']}),
    ]
    list_display = ('word_lemma', 'date_said', 'week_number_said')
    search_fields = ['word_lemma']
    list_filter = ['date_said']
    orderning = ['-date_said']


admin.site.register(LemmaCounter, LemmaCounterAdmin)
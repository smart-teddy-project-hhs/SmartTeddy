import pytest
from django.utils import timezone
import datetime
from speechrecognition.models import SaidLemma


class TestLemmaCounter:

    def test_lemma_was_recently_said_with_equal_date(self):
        time = timezone.now() - datetime.timedelta(days=7)
        future_lemma = SaidLemma(date_said=time)
        assert future_lemma.was_said_last_week() is False

    def test_lemma_was_recently_said_with_before_date(self):
        time = timezone.now() - datetime.timedelta(days=6, hours=23, minutes=59)
        equal_lemma = SaidLemma(date_said=time)
        assert equal_lemma.was_said_last_week() is True

    def test_lemma_was_recently_said_with_future_date(self):
        time = timezone.now() + datetime.timedelta(seconds=1)
        equal_lemma = SaidLemma(date_said=time)
        assert equal_lemma.was_said_last_week() is False

    def test_lemma_was_recently_said_with_date_now(self):
        time = timezone.now()
        equal_lemma = SaidLemma(date_said=time)
        assert equal_lemma.was_said_last_week() is True


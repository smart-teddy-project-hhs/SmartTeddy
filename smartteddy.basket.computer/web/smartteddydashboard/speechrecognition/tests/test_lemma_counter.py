import pytest
from django.utils import timezone
import datetime
from speechrecognition.models import LemmaCounter, validate_week_number


class TestLemmaCounter:

    def test_lemma_was_recently_said_with_equal_date(self):
        time = timezone.now() - datetime.timedelta(days=7)
        future_lemma = LemmaCounter(date_said=time)
        assert future_lemma.was_said_last_week() is False

    def test_lemma_was_recently_said_with_before_date(self):
        time = timezone.now() - datetime.timedelta(days=6, hours=23, minutes=59)
        equal_lemma = LemmaCounter(date_said=time)
        assert equal_lemma.was_said_last_week() is True

    def test_lemma_was_recently_said_with_future_date(self):
        time = timezone.now() + datetime.timedelta(seconds=1)
        equal_lemma = LemmaCounter(date_said=time)
        assert equal_lemma.was_said_last_week() is False

    def test_lemma_was_recently_said_with_date_now(self):
        time = timezone.now()
        equal_lemma = LemmaCounter(date_said=time)
        assert equal_lemma.was_said_last_week() is True

    def test_is_last_week_number_in_year(self):
        last_week_number = 53
        validate_week_number(last_week_number)

    def test_is_first_week_number_in_year(self):
        last_week_number = 1
        validate_week_number(last_week_number)

    def test_is_week_number_before_in_year(self):
        with pytest.raises(Exception):
            last_week_number = 0
            validate_week_number(last_week_number)

    def test_is_week_number_after_in_year(self):
        with pytest.raises(Exception):
            last_week_number = 54
            validate_week_number(last_week_number)

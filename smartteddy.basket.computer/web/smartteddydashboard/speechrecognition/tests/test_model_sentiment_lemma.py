from speechrecognition.models import SentimentLemma

POSITIVE = "POS"
NEGATIVE = "NEG"


def create_sentiment_lemma(lemma, is_positive=False):
    polarity_of_sentiment = POSITIVE if is_positive else NEGATIVE
    sentiment_lemma = SentimentLemma(sentiment_polarity=polarity_of_sentiment, lemma_written_form=lemma)
    return sentiment_lemma


class TestModelSentimentLemma:

    def test_sentiment_lemma_is_postive(self):
        positive_lemma = create_sentiment_lemma(lemma="goed", is_positive=True)
        assert positive_lemma.is_positive is True

    def test_sentiment_lemma_is_negative(self):
        positive_lemma = create_sentiment_lemma(lemma="slecht", is_positive=False)
        assert positive_lemma.is_positive is False

    def test_sentiment_lemma_is_negative_wben_none(self):
        positive_lemma = create_sentiment_lemma(lemma="slecht", is_positive=None)
        assert positive_lemma.is_positive is False

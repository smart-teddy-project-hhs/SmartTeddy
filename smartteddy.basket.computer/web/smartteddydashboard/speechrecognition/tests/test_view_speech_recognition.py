from django.test import Client


class TestViewSpeechRecognition:

    def test_raises_400_no_data_is_applied(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_json_body_is_empty(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_text_is_misspelled_in_speech_recognition_sentence(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"result": [], "texts": ""},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_result_is_misspelled_in_speech_recognition_sentence(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"result": [], "texts": ""},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_text_is_misspelled_in_speech_recognition_sentence(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"result": [], "texts": ""},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_text_is_missing_in_speech_recognition_sentence(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"result": []},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_400_when_result_is_missing_in_speech_recognition_sentence(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"text": []},
            content_type='application/json'
        )
        assert response.status_code == 400

    def test_raises_200_when_result_is_missing_word(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={"result": [], "text": ""},
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_raises_http_400_when_word_is_missing_from_result(self):
        http_client = Client()
        response = http_client.post(
            path='/speech-recognition/sentence',
            data={
                "result": [{
                    "conf": 0.732019,
                    "end": 9.180000,
                    "start": 8.730000,
                }],
                "text": "goed"
            },
            content_type='application/json'
        )
        assert response.status_code == 400

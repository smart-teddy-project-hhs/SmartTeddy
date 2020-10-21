# Generated by Django 3.1.2 on 2020-10-19 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentLemma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemma_written_form', models.CharField(max_length=100)),
                ('sense_confidence_level', models.CharField(max_length=100)),
                ('sentiment_polarity', models.CharField(choices=[('POS', 'positive'), ('NEG', 'negative')], default='NEG', max_length=3)),
                ('part_of_speech', models.CharField(choices=[('ADJE', 'ADJE'), ('NOUN', 'NOUN'), ('VERB', 'VERB')], default='VERB', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='LemmaCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_said', models.DateTimeField(verbose_name='Date said on')),
                ('sentiment_lemma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='speech_recognition.sentimentlemma')),
            ],
        ),
    ]
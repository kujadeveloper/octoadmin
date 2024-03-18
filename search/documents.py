import os

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl import fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer, token_filter, char_filter
from .models import OctoModel

turkish_lowercase = token_filter(
    'turkish_lowercase',
    type='lowercase',
    language='turkish'
)


turkish_lowercase = token_filter('turkish_lowercase', type='lowercase', language='turkish')
html_strip = char_filter('html_strip', type='html_strip')

text_analyzer = analyzer(
    'text_analyzer',
    tokenizer='standard',
    filter=[turkish_lowercase, 'stop', 'snowball'],
    char_filter=[html_strip]
)

@registry.register_document
class OctoDocument(Document):
    id = fields.IntegerField(attr='id')

    class Index:
        name = 'octoxlabsdata'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = OctoModel
        fields = [
            'Hostname',
            'Ip'
        ]
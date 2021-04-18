# coding: utf-8
import json
from django.template.response import TemplateResponse
def json_format(data):
    if isinstance(data, dict):
        json.dumps(data, indent=4)

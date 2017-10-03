# -*- coding: utf-8 -*-
import os

import requests

from notify import get_elapsed_time, channels, result_color, build_result, download_link


def build_message():
    repository = os.getenv('WERCKER_GIT_REPOSITORY')
    branch = os.getenv('WERCKER_GIT_BRANCH')
    result = os.getenv('WERCKER_RESULT')

    fields = [{
        'title': 'Time',
        'value': get_elapsed_time(),
        'short': True
    }]
    # only add a download link if the build was a success
    if build_result():
        fields.append({
            'title': 'Download',
            'value': download_link(),
            'short': True
        })
    message_data = {
        'icon_url': os.getenv("ANDROID_DEPLOY_NOTIFY_ICON_URL"),
        'attachments': [{
            'title': '{}:{} – build {}'.format(repository, branch, result),
            'title_link': os.getenv('WERCKER_BUILD_URL'),
            'fields': fields,
            'color': result_color(),
        }]
    }
    _send(message_data)


def _send(message_data):
    webhook_url = os.environ["ANDROID_DEPLOY_NOTIFY_WEBHOOK_URL"]
    for channel in channels():
        message_data['channel'] = channel
        requests.post(webhook_url, json=message_data)

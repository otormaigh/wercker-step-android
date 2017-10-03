# -*- coding:utf-8 -*-
import calendar
import os

import datetime


def spliterator(bad_string):
    """Split a comma separated string into a list, removing any white space while your there."""
    if bad_string:
        return bad_string.replace(' ', '').split(',')


def build_result():
    result = os.environ['WERCKER_RESULT']
    if result and result == 'failed':
        return False
    else:
        return True


def channels():
    if build_result():
        notify_success = os.getenv('ANDROID_DEPLOY_NOTIFY_NOTIFY_SUCCESS')
        return spliterator(notify_success)
    else:
        notify_fail = os.getenv('ANDROID_DEPLOY_NOTIFY_NOTIFY_FAIL')
        return spliterator(notify_fail)


def get_elapsed_time():
    """Return in hours and minutes how long the pipeline took to complete."""
    started = int(os.environ['WERCKER_MAIN_PIPELINE_STARTED'])
    now = datetime.datetime.utcnow()
    finished = calendar.timegm(now.utctimetuple())
    elapsed = finished - started
    return hours_minutes(elapsed)


def hours_minutes(seconds):
    """Convert seconds into hours and minutes."""
    m, s = divmod(seconds, 60)
    mins = pluralize(m, 'minute')
    secs = pluralize(s, 'second')
    if mins:
        return mins + ' ' + secs
    return secs


def pluralize(number, word):
    """Pluralize the word based on the number."""
    if number:
        phrase = '%s %s' % (number, word)
        if number != 1:
            phrase += 's'
        return phrase
    return ''


def result_color():
    if build_result():
        return '#2ECC71'
    else:
        return '#EC7063'


def download_link():
    url = os.getenv('BUCKET_URL')
    build_type = os.getenv('ANDROID_DEPLOY_NOTIFY_BUILD_TYPE')
    base_name = os.getenv('BASE_NAME')
    apk_name = "{}-{}.apk".format(base_name.split('##BASE_NAME[', 1)[1].split(']')[0], build_type)
    return "<{}|{}>".format(url + apk_name, apk_name)

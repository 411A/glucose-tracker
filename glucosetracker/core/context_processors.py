from django.conf import settings


def third_party_tracking_ids(request):
    """
    Retrieve 3rd-party tracking IDs from the settings file and add them to the
    request context.
    """
    return {
        'google_analytics_tracking_id': settings.GOOGLE_ANALYTICS_TRACKING_ID,
        'intercom_app_id': settings.INTERCOM_APP_ID,
        'sharethis_publisher_id': settings.SHARETHIS_PUBLISHER_ID,
    }

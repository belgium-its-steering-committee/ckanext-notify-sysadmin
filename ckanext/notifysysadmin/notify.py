import logging

from ckan.common import config
from ckan.lib.mailer import mail_user

log = logging.getLogger(__name__)

NOTIFICATION_SPACING = 45


def notify_sysadmins(sysadmins, entity):
    site_url = config.get('ckan.site_url', "")
    organization_url = "{0}/organization/{1}"
    subject = u"New organization {0} created!".format(entity.title)
    message = u"""
    A new organization {0} has been created on {1}.
    As a system administrator, you can delete this organization if it doesn't fulfill the required standards. 
    
    {2}
    
    Regards
    """.format(
        entity.title,
        entity.created.strftime("%d-%m-%Y, %H:%M:%S"),
        organization_url.format(site_url, entity.name)
    )
    for sysadmin in sysadmins:
        try:
            mail_user(sysadmin, subject, message)
        except Exception as e:
            log.exception("Mail (notify_sysadmins) could not be sent")


def print_notification(entity):
    log.info(u"Organisation {0} created".format(entity.name))
    log.info(_notification_line_spacer())
    log.info(u"| id          | {0} |".format(_notification_format_value(entity.id)))
    log.info(_notification_line_spacer())
    log.info(u"| name        | {0} |".format(_notification_format_value(entity.name)))
    log.info(_notification_line_spacer())
    log.info(u"| title       | {0} |".format(_notification_format_value(entity.title)))
    log.info(_notification_line_spacer())
    log.info(u"| created     | {0} |".format(_notification_format_value(entity.created.strftime("%d-%m-%Y, %H:%M:%S"))))
    log.info(_notification_line_spacer())


def _notification_line_spacer():
    return "+-------------+" + "-" * NOTIFICATION_SPACING + "+"


def _notification_format_value(value):
    nfv_length = NOTIFICATION_SPACING - 2 - len(value)
    return value + " " * nfv_length

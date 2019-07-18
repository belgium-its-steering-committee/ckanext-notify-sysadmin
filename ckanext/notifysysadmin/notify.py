import logging

from ckan.lib.mailer import mail_user

log = logging.getLogger(__name__)

NOTIFICATION_SPACING = 45


def notify_sysadmins(sysadmins, entity):
    subject = "New organization {0} created!".format(entity.title)
    message = """
    A new organization {0} has been created on {1}.
    As a system administrator, you can delete this organization if it doesn't fulfill the required standards. 
    
    Regards
    """.format(entity.title, entity.created.strftime("%d-%m-%Y, %H:%M:%S"))
    print("#"*35)
    print(entity)
    print("#"*35)
    for sysadmin in sysadmins:
        try:
            mail_user(sysadmin, subject, message)
        except Exception as e:
            log.exception("Mail (notify_sysadmins) could not be sent", e)


def print_notification(entity):
    log.info("Organisation {0} created".format(entity.name))
    log.info(_notification_line_spacer())
    log.info("| id          | {0} |".format(_notification_format_value(entity.id)))
    log.info(_notification_line_spacer())
    log.info("| name        | {0} |".format(_notification_format_value(entity.name)))
    log.info(_notification_line_spacer())
    log.info("| title       | {0} |".format(_notification_format_value(entity.title)))
    log.info(_notification_line_spacer())
    log.info("| created     | {0} |".format(_notification_format_value(entity.created.strftime("%d-%m-%Y, %H:%M:%S"))))
    log.info(_notification_line_spacer())


def _notification_line_spacer():
    return "+-------------+" + "-" * NOTIFICATION_SPACING + "+"


def _notification_format_value(value):
    nfv_length = NOTIFICATION_SPACING - 2 - len(value)
    return value + " " * nfv_length

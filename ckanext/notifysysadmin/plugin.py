import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

NOTIFICATION_SPACING = 45


class NotifySysadminPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IOrganizationController, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'notifysysadmin')

    # IOrganizationController

    def create(self, entity):
        _print_notification(entity)


def _print_notification(entity):
    print("Organisation {0} created".format(entity.name))
    print(_notification_line_spacer())
    print("| id          | {0} |".format(_notification_format_value(entity.id)))
    print(_notification_line_spacer())
    print("| name        | {0} |".format(_notification_format_value(entity.name)))
    print(_notification_line_spacer())
    print("| title       | {0} |".format(_notification_format_value(entity.title)))
    print(_notification_line_spacer())
    print("| created     | {0} |".format(_notification_format_value(entity.created.strftime("%m/%d/%Y, %H:%M:%S"))))
    print(_notification_line_spacer())


def _notification_line_spacer():
    return "+-------------+" + "-" * NOTIFICATION_SPACING + "+"


def _notification_format_value(value):
    nfv_length = NOTIFICATION_SPACING - 2 - len(value)
    return value + " " * nfv_length

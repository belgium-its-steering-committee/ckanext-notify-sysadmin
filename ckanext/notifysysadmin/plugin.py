import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from sysadmin import get_ckan_sysadmins
from notify import print_notification, notify_sysadmins


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
        print_notification(entity)
        sysadmins = get_ckan_sysadmins()
        notify_sysadmins(sysadmins, entity)

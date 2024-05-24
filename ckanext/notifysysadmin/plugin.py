import ckan.plugins as plugins #type:ignore
import ckan.plugins.toolkit as toolkit #type:ignore

from sysadmin import get_ckan_sysadmins
from notify import notify_sysadmins


class NotifySysadminPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IOrganizationController, inherit=True)

    # IOrganizationController
    def create(self, entity):
        sysadminsList = get_ckan_sysadmins()
        notify_sysadmins(sysadminsList, entity)

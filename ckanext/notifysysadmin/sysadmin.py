from ckan import model


def get_ckan_sysadmins():
    sysadmins = set(model.Session.query(model.User).filter(model.User.sysadmin == True))
    sysadmins = set([sysadmin for sysadmin in sysadmins if not sysadmin.email.find("@localhost")])
    return sysadmins

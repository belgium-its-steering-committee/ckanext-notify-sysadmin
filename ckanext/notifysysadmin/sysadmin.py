from ckan import model


def get_ckan_sysadmins():
    sysadmins = set(model.Session.query(model.User).filter(model.User.sysadmin == True))
    sysadmins = set([sysadmin for sysadmin in sysadmins if sysadmin.email
                     is not None and not sysadmin.email.find("@localhost")])
    return sysadmins

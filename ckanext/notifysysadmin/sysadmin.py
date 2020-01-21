from ckan import model


def get_ckan_sysadmins():
    sysadmins = set(model.Session.query(model.User).filter(model.User.sysadmin == True))
    for sysadmin in sysadmins:
        print(sysadmin)
        print(sysadmin.email)
    sysadmins = set([sysadmin for sysadmin in sysadmins if sysadmin.email
                     is not None and not sysadmin.email.find("@localhost")])
    return sysadmins

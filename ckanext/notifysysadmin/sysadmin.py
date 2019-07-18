from ckan import model


def get_ckan_sysadmins():
    sysadmins = set(model.Session.query(model.User).filter(model.User.sysadmin == True))
    return sysadmins

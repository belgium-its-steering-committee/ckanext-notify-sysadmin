import ckan.model as model #type:ignore

def get_ckan_sysadmins():
    sysadmins = model.Session.query(model.User)\
        .filter(model.User.sysadmin == True)\
        .filter(model.User.email != None)\
        .filter(model.User.email != '')\
        .all()
    return sysadmins

from flask_security.models import fsqla_v3 as fsqla
from extensions.alchemy import db

fsqla.FsModels.set_db_info(db)


class Role(db.Model, fsqla.FsRoleMixin):
    pass


class User(db.Model, fsqla.FsUserMixin):
    pass

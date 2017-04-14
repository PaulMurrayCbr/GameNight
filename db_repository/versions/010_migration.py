from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
bonus_type = Table('bonus_type', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('stacking', Boolean),
)

effect = Table('effect', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('buff_id', INTEGER),
    Column('type', VARCHAR(length=64)),
    Column('target', VARCHAR(length=64)),
    Column('bounus', INTEGER),
    Column('ablative', BOOLEAN),
    Column('recursive_buf_id', INTEGER),
)

effect = Table('effect', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('buff_id', Integer),
    Column('bonustype_id', Integer),
    Column('target', String(length=64)),
    Column('bounus', Integer),
    Column('ablative', Boolean),
    Column('recursive_buf_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bonus_type'].create()
    pre_meta.tables['effect'].columns['type'].drop()
    post_meta.tables['effect'].columns['bonustype_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['bonus_type'].drop()
    pre_meta.tables['effect'].columns['type'].create()
    post_meta.tables['effect'].columns['bonustype_id'].drop()

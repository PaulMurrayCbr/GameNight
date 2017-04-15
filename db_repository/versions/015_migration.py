from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
active_effect = Table('active_effect', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('characterid', Integer),
    Column('sourceid', Integer),
    Column('bonustype', String(length=64)),
    Column('bonusto', String(length=64)),
    Column('bounusamt', Integer),
    Column('zock', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['active_effect'].columns['zock'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['active_effect'].columns['zock'].drop()

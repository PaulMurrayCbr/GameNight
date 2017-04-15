from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
active_effect = Table('active_effect', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('characterid', INTEGER),
    Column('bonustype', VARCHAR(length=64)),
    Column('bounusamt', INTEGER),
    Column('bonusto', VARCHAR(length=64)),
    Column('sourceid', INTEGER),
    Column('zock', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['active_effect'].columns['bounusamt'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['active_effect'].columns['bounusamt'].create()

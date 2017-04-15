from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
buff = Table('buff', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('character_id', INTEGER),
    Column('name', VARCHAR(length=64)),
    Column('duration_unit', VARCHAR(length=64)),
    Column('duration', INTEGER),
)

cast_effect = Table('cast_effect', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('caston_id', INTEGER),
    Column('effect_id', INTEGER),
    Column('ablative_remaining', INTEGER),
)

cast_on = Table('cast_on', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('casting_id', INTEGER),
    Column('character_id', INTEGER),
    Column('enabled', BOOLEAN),
)

casting = Table('casting', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('buff_id', INTEGER),
    Column('duration_remaining', INTEGER),
    Column('bounus', INTEGER),
)

effect = Table('effect', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('buff_id', INTEGER),
    Column('target', VARCHAR(length=64)),
    Column('bounus', INTEGER),
    Column('ablative', BOOLEAN),
    Column('recursive_buf_id', INTEGER),
    Column('bonustype', VARCHAR(length=64)),
)

active_effect = Table('active_effect', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('characterid', Integer),
    Column('bonustype', String(length=64)),
    Column('bousto', String(length=64)),
    Column('bounusamt', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['buff'].drop()
    pre_meta.tables['cast_effect'].drop()
    pre_meta.tables['cast_on'].drop()
    pre_meta.tables['casting'].drop()
    pre_meta.tables['effect'].drop()
    post_meta.tables['active_effect'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['buff'].create()
    pre_meta.tables['cast_effect'].create()
    pre_meta.tables['cast_on'].create()
    pre_meta.tables['casting'].create()
    pre_meta.tables['effect'].create()
    post_meta.tables['active_effect'].drop()

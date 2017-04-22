from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
buff_on = Table('buff_on', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('character_id', Integer),
    Column('buff_id', Integer),
    Column('supressed', Boolean),
    Column('notes', String(length=1023)),
)

buff = Table('buff', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('character_id', Integer),
    Column('description', String(length=1023)),
    Column('duration_unit', String(length=10)),
    Column('duration', Integer),
    Column('current_duration', Integer),
    Column('supressed', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buff_on'].create()
    post_meta.tables['buff'].columns['current_duration'].create()
    post_meta.tables['buff'].columns['supressed'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buff_on'].drop()
    post_meta.tables['buff'].columns['current_duration'].drop()
    post_meta.tables['buff'].columns['supressed'].drop()

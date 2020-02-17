import sqlalchemy as sa
from sqlalchemy import Table, Column, BigInteger, VARCHAR, DateTime, Date


def check_core_tbls(engine: sa.engine):
    maybe_make_person_tbl(engine)
    maybe_make_app_list__tbl(engine)


def maybe_make_app_list__tbl(engine):
    if engine.has_table('app_list'):
        print('app_list table exists')
    else:
        meta = sa.MetaData()
        app_tbl = Table('app_list', meta,
            Column('a_key', BigInteger, primary_key=True),
            Column('app_name', VARCHAR(length=100))
        )
        app_tbl.create(engine)


def maybe_make_person_tbl(engine):
    if engine.has_table('person'):
        print('person table exists')
    else:
        meta = sa.MetaData()
        person_tbl = Table('person', meta,
            Column('p_key', BigInteger, primary_key=True),
            Column('name', VARCHAR(length=200)),
            Column('timestamp', VARCHAR(length=50)),
            Column('contact', VARCHAR(length=100)),
            Column('positions', VARCHAR(length=100)),
            Column('resp_email_dt', Date),
            Column('set_interview_dt', Date),
            Column('interview_actual_dt', Date),
            Column('ss_and_photo', VARCHAR(length=10)),
            Column('passport', VARCHAR(length=10)),
            Column('bcheck_auth_dt', Date),
            Column('bcheck_rec_dt', Date),
            Column('told_supervisor', VARCHAR(10)),
            Column('accept_email', VARCHAR(20)),
            Column('newsletter', VARCHAR(10)),
            Column('first_day', Date),
            Column('orientation', Date),
            Column('welcome_survey', VARCHAR(20)),
            Column('waitlist', VARCHAR(20)),
            Column('notes', VARCHAR(500))
            )
        person_tbl.create(engine)


def check_tbl(engine, tbl_name):
    res = engine.execute('SELECT * FROM {}'.format(tbl_name))
    print('keys:')
    for key in res.keys():
        print(key)
    print('some rows')
    for _ in range(0,3):
        print(res.fetchone())
    res.close()

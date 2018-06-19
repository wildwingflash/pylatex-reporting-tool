# ----------------------------
# Turn Foreign Key Constraints ON for
# each connection.
# ----------------------------
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Evidence, Project, create_database
from datetime import datetime
import os


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


if not os.path.exists('/database/my_db_tests.sqlite'):
    create_database()

engine = create_engine('sqlite:///database/my_db_tests.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def create(element):
    session.add(element)
    session.commit()
    return element


def delete(element):
    session.delete(element)
    session.commit()


def commit_changes():
    session.commit()


def get_evidence_by_id(evidence_id):
    return session.query(Evidence).filter(Evidence.id == evidence_id)


def get_evidences_by_project_name(project_id):
    return session.query(Evidence).filter(Evidence.project_id == project_id).all()


def get_project_by_name(project_name):
    return session.query(Project).filter(Project.name == project_name).one_or_none()


def get_all_projects():
    return session.query(Project).all()

# ----------------------------
# Populate the database
# ----------------------------
evidence_2 = Evidence(name='ssssssss',
                      file_path='/root/Desktop/test.txt',
                      description='lasdkfasd alkdf asdf adf ajdsf kasdf asdf ladksf lakjsdf lkajsdf')


project_66 = Project(name='myprojectGOOOOD',
                     description="my general description",
                     evidences=[evidence_2])
print(get_all_projects())
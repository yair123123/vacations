
from app.db.models import Base
from app.db.repository.country_repository import add_all_countries
from app.db.repository.csv_repository import insert_all_csv_to_db
from app.db.services.api_service import create_objects_countries

from app.settings.config import  engine


def init_db():
   Base.metadata.drop_all(engine)
   Base.metadata.create_all(engine)
def fill_db():
   insert_all_csv_to_db()
   add_all_countries(create_objects_countries())

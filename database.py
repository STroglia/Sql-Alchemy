from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///usuarios.db"  # O el nombre de tu base de datos

# Motor de base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Fábrica de sesiones
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Modelo Base declarativo para que los modelos lo hereden
class Base(DeclarativeBase):
    pass
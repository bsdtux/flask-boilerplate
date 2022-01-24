""" API Configuration module """
import os
import typing as ty

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

C = ty.TypeVar("C")


class DatabaseEngine:
    @staticmethod
    def create_db_engine(app_env: str):
        db_engine = os.environ.get("DB_ENGINE")

        if not db_engine:
            engine_path = os.path.join(BASE_DIR, f"./data/api_{app_env}.dat")
            return f"sqlite://${engine_path}"

        return ""


class BaseConfig(ty.Generic[C]):
    """Base Config"""

    DEBUG: bool = True
    TESTING: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(BaseConfig):
    """Development Config"""


class TestConfig(BaseConfig):
    """Testing Config"""

    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = DatabaseEngine.create_db_engine("testing")


class ProdConfig(BaseConfig):
    """Production Config"""

    DEBUG: bool = False
    TESTING: bool = False


class FactoryConfig:
    @staticmethod
    def create_config(app_override: str = "") -> C:
        app_env = app_override or os.environ.get("FLASK_ENV") or "development"
        config_map = {
            "development": DevConfig,
            "testing": TestConfig,
            "production": ProdConfig,
        }
        config_obj = config_map.get(app_env) or DevConfig
        return config_obj

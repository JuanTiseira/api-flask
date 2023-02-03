"""
"""


class LocalConfig:
    ENV = "local"
    AUTH_URL = "http://127.0.0.1:5000"
    FUNCTION_URL = ""


class ProductionConfig:
    ENV = "prod"
    AUTH_URL = "http://127.0.0.1:5000"
    FUNCTION_URL = ""


config = {
    "local": LocalConfig,
    "production": ProductionConfig,
}

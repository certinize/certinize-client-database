from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    class Config(AppSettings.Config):
        ...

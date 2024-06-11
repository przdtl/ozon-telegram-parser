from pathlib import Path
from pydantic_settings import (BaseSettings, SettingsConfigDict)


class Settings(BaseSettings):

    BOT_TOKEN: str
    PATH_TO_EXCEL_FOLDER: str = str(
        Path(__file__).resolve().parent.parent.parent) + "\\media\\excel\\"

    ALLOWED_EXCEL_EXTENTIONS: list[str] = ['.xls', '.xlsx']

    #
    OZON_PRODUCT_URL: str = 'https://www.ozon.ru/product'
    PRICE_PARSER_SERVICE_URL: str = 'http://127.0.0.1:8000'
    OZON_PRICE_PARSER_SERVICE_URL: str = PRICE_PARSER_SERVICE_URL + '/ozon'
    # TODO: add wildberries support

    model_config = SettingsConfigDict(env_file='.env')
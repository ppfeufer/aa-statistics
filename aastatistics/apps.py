from django.apps import AppConfig
from aastatistics import __version__


class AastatisticsConfig(AppConfig):
    name = 'aastatistics'
    label = 'aastatistics'
    verbose_name = f"Statistics v{__version__}"

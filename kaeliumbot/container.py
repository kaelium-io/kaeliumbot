from dependency_injector import containers, providers

from kaeliumbot.settings import Settings


class Container(containers.DeclarativeContainer):
    settings = providers.Singleton(Settings)

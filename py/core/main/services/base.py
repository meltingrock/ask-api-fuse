from abc import ABC

from ..abstractions import FUSEProviders
from ..config import FUSEConfig


class Service(ABC):
    def __init__(
        self,
        config: FUSEConfig,
        providers: FUSEProviders,
    ):
        self.config = config
        self.providers = providers

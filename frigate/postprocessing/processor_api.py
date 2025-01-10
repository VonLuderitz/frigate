import logging
from abc import ABC, abstractmethod

import numpy as np

from frigate.config import FrigateConfig

from .types import PostProcessingMetrics

logger = logging.getLogger(__name__)


class ProcessorApi(ABC):
    @abstractmethod
    def __init__(self, config: FrigateConfig, metrics: PostProcessingMetrics) -> None:
        self.config = config
        self.metrics = metrics
        pass

    @abstractmethod
    def process_frame(self, obj_data: dict[str, any], frame: np.ndarray) -> None:
        """Processes the frame with object data.
        Args:
            obj_data (dict): containing data about focused object in frame.
            frame (ndarray): full yuv frame.

        Returns:
            None.
        """
        pass

    @abstractmethod
    def handle_request(self, request_data: dict[str, any]) -> dict[str, any] | None:
        """Handle metadata requests.
        Args:
            request_data (dict): containing data about requested change to process.

        Returns:
            None if request was not handled, otherwise return response.
        """
        pass

    @abstractmethod
    def expire_object(self, object_id: str) -> None:
        """Handle objects that are no longer detected.
        Args:
            object_id (str): id of object that is no longer detected.

        Returns:
            None.
        """
        pass

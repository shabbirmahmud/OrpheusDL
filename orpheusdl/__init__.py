"""
OrpheusDL - A modular music archival program

This package provides a modular framework for downloading and archiving music
from various streaming services.
"""

__version__ = "1.0.0"
__author__ = "OrfiTeam"
__email__ = "contact@orfi.dev"

# Import main classes and functions for easy access
from .core import Orpheus, orpheus_core_download
from .music_downloader import Downloader, beauty_format_seconds

__all__ = [
    "Orpheus",
    "orpheus_core_download",
    "Downloader",
    "beauty_format_seconds",
]
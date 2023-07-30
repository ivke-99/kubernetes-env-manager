"""
kubernetes-env-manager package
"""
import os

__version__ = os.getenv("APP_VERSION", "0.0.0")

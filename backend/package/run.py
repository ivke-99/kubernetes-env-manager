from uvicorn import run
import os
import logging
import logging.config

log_level = os.getenv("LOG_LEVEL", "DEBUG")
logging_config = {
    "version": 1,
    "disable_exiting_loggers": True,
    "formatters": {
        "default": {
            "format": "%(asctime)s] %(levelname)s in %(module)s - %(name)s: %(message)s",
        },
    },
    "loggers": {
        "multipart": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "main": {"level": log_level, "handlers": ["console"]},
        "app": {"level": log_level, "handlers": ["console"]},
        "package": {"level": log_level, "handlers": ["console"]},
        "uvicorn": {"handlers": ["console"], "level": "ERROR", "propagate": False},
        "uvicorn.error": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
    "handlers": {
        "console": {
            "level": log_level,
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
}
logger = logging.getLogger("main")


def dev():
    run(
        "package.app.start:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level=log_level.lower(),
        log_config=logging_config,
    )


def prod():
    run(
        "package.app.start:app",
        headers=[
            ("server", "Apache"),
            ("X-Frame-Options", "SAMEORIGIN"),
            ("X-XSS-Protection", "1; mode=block"),
            ("X-Content-Type-Options", "nosniff"),
            ("Strict-Transport-Security", "max-age=15768000; includeSubDomains"),
            ("Referrer-Policy", "no-referrer-when-downgrade"),
            ("Content-Security-Policy", "frame-ancestors 'self'"),
        ],
        host="0.0.0.0",
        port=80,
        log_level=log_level.lower(),
        log_config=logging_config,
        forwarded_allow_ips="*",
    )


if __name__ == "__main__":
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    dev()

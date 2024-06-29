# Standard Library
import argparse
import os

# External Libraries
from alembic import command
from alembic.config import Config

# VerdanTech Source
from src import settings

# Find the directory where this script is located
current_directory = os.path.dirname(os.path.abspath(__file__))
config_directory = os.path.join(current_directory, "alembic.ini")
script_location = os.path.join(current_directory, "alembic/")

def reset_migrations():
    """
    Script to reset the migrations.
    """
    alembic_cfg = Config(config_directory)
    alembic_cfg.set_main_option("sqlalchemy.url", settings.ALCHEMY_URI)
    alembic_cfg.set_main_option("script_location", script_location)

    # Downgrade to the base
    command.downgrade(alembic_cfg, "base")
    # Upgrade to the head
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reset database migrations")
    parser.add_argument("--reset", action='store_true', help="Reset all migrations")
    args = parser.parse_args()
    
    if args.reset:
        reset_migrations()
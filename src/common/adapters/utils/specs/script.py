# In main.py
from .manager import spec_manager

# Make sure to import your other files so their specs are registered
import src.user.domain.specs

if __name__ == "__main__":
    spec_manager.dump_to_json("specs.json")
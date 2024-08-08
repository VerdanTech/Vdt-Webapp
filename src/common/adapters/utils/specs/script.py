# In main.py
from .manager import spec_manager

if __name__ == "__main__":
    with open("specs.json", "w") as file:
        # Make sure to import all files so their specs are registered
        # VerdanTech Source
        import src.user.domain.specs

        json = spec_manager.to_json()
        file.write(json)

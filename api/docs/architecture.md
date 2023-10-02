# Clean architecture

# This repos architecture

Base provider - add the actual providing functions into the dict key for example user_motor_repo_provider = {"user_repo": provide_user_motor_repo}

Consolidation provider - consolidate multiple dicts through merge for example motor_repo_provider = (user_motor_repo_provider | garden_motor_repo_provider)
Choice provider - select one dict to use for example repo_provider = motor_repo_providre
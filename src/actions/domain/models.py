# Standard Library
from datetime import datetime

# VerdanTech Source
from src.common.domain import (
    Ref,
    RootEntity,
    Value,
    root_entity_transform,
    value_transform,
)
from src.user.domain import User

from .enums import ActionEnum


@value_transform
class Reminder(Value):
    time: datetime
    title: str
    description: str | None = None


@root_entity_transform
class Action(RootEntity):
    action_type: ActionEnum | str
    # time_window: TimeWindow
    reminders: set[Reminder]
    assignees: set[Ref[User]]
    title: str
    description: str | None = None

    def dismiss(self):
        """dismiss the action"""

    def update(self):
        """bring action up to a date"""

    def complete(self):
        """complete an action"""

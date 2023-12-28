"""
The "bluetooth commands" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the bluetooth_commands component you will need to add the following to your
configuration.yaml file.

bluetooth_commands:
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.components import bluetooth

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "bluetooth_commands"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('bluetooth_commands.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True

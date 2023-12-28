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

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "bluetooth_commands"

ATTR_NAME = "name"
DEFAULT_NAME = "World"

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    def handle_hello(call):
        """Handle the service call."""
        name = call.data.get(ATTR_NAME, DEFAULT_NAME)

        hass.states.set("bluetooth_commands.hello", name)
    
    hass.services.register(DOMAIN, "hello", handle_hello)

    # Return boolean to indicate that initialization was successfully.
    return True

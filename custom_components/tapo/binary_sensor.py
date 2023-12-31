from typing import cast

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from custom_components.tapo.const import DOMAIN
from custom_components.tapo.coordinators import HassTapoDeviceData
from custom_components.tapo.sensor import TapoSensor
from custom_components.tapo.sensors import OverheatSensorSource


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_devices):
    # get tapo helper
    data = cast(HassTapoDeviceData, hass.data[DOMAIN][entry.entry_id])
    sensors = [TapoSensor(data.coordinator, OverheatSensorSource())]
    async_add_devices(sensors, True)

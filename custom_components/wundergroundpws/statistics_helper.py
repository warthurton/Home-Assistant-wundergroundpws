"""
Helper to get statistics unit of measurement for an entity from Home Assistant statistics.
"""
from homeassistant.components.recorder.statistics import get_metadata
from homeassistant.const import UnitOfTemperature, UnitOfLength, UnitOfSpeed, UnitOfPressure

async def async_get_statistics_unit(hass, entity_id):
    """Return the unit of measurement from statistics metadata for the given entity_id, or None if not found."""
    # get_metadata returns a dict of metadata for all statistics, filter for our entity_id
    stats = await hass.async_add_executor_job(get_metadata, hass, None, False)
    meta = stats.get(entity_id)
    if meta and "unit_of_measurement" in meta:
        return meta["unit_of_measurement"]
    return None

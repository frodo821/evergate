"""
"""
from pydantic import BaseModel, Field
from evergate.datamodel.item import LocationFlag


class Blueprint(BaseModel):
  """A data model for a blueprint.

  Attributes:
    item_id (int): Unique ID for this item.
    location_flag (LocationFlag): indicates what type container of location_id is.
    location_id (int): References a station, a ship or an item_id if this blueprint is located within a container. If the return value is an item_id, then the Character AssetList API must be queried to find the container using the given item_id to determine the correct location of the Blueprint.
    material_efficiency (int): The material efficiency level of this blueprint.
    quantity (int): A range of numbers with a minimum of -2 and no maximum value where -1 is an original and -2 is a copy. It can be a positive integer if it is a stack of blueprint originals fresh from the market (e.g. no activities performed on them yet).
    runs (int): Number of runs remaining if the blueprint is a copy, -1 if it is an original.
    time_efficiency (int): The time efficiency level of this blueprint.
    type_id (int): The type ID of the blueprint.
  """

  item_id: int = Field(description="Unique ID for this item.")
  location_flag: LocationFlag = Field(
      description="indicates what type container of location_id is.")
  location_id: int = Field(description=(
      "References a station, a ship or an item_id if this blueprint is located within a container. "
      "If the return value is an item_id, then the Character AssetList API must be queried to "
      "find the container using the given item_id to determine the correct location of the Blueprint."
  ))
  material_efficiency: int = Field(
      description="The material efficiency level of this blueprint.")
  quantity: int = Field(description=(
      "A range of numbers with a minimum of -2 and no maximum value where -1 is an original and -2 is a copy. "
      "It can be a positive integer if it is a stack of blueprint originals fresh from the market "
      "(e.g. no activities performed on them yet)."))
  runs: int = Field(
      description=
      "Number of runs remaining if the blueprint is a copy, -1 if it is an original."
  )
  time_efficiency: int = Field(
      description="The time efficiency level of this blueprint.")
  type_id: int = Field(
      description="The id of the product item of this blueprint.")
from .entity_artifact import EntityArtifact
class Slot(EntityArtifact):
  fields = frozenset(('x', 'y', 'z'))
  min_x = 0
  max_x = 0
  min_y = 0
  max_y = 0
  min_z = 0 
  max_z = 0
  item = None
  def to_dict( self ):
	slot_dict = dict(
		id=self.id,
		item=self.item.to_dict(),
		min_x=self.min_x,
		max_x=self.max_x,
		min_y=self.min_y,
		max_y=self.max_y,
		min_z=self.min_z,
		max_z=self.max_z )
	if self.item is None:
		return slot_dict
	slot_dict['item'] = self.item.to_dict()
	return slot_dict
  @classmethod
  def from_space_and_item(cls, space, item):
	slot = Slot( 
	  min_x=space.x,
	  min_y=space.y,
	  min_z=space.z,
	  max_x=space.x_with_item(item),
	  max_y=space.y_with_item(item),
	  max_z=space.z_with_item(item))
	slot.set_item( item )
	return slot
  def get_coords(self):
    return self.get_position()
  def set_item(self, value):
    self.item = value


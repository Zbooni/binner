from .algo import Algo
from .entity_slot import Slot
from . import log, show_adding_box_log, find_smallest
from .exception import DistributionException
import time
class AlgoSmallest(Algo):
  """
  find the smallest bin
  for a given amount of 
  bins.

  Output SHOULD try to have all
  the items. I.e 

  A bin smaller bin with less items is worse than 
  A bigger bin with more items

  @param item_collection: set of items

  @returns a Bin object
         whose size is smallest with the most
         amount of items 
  """
  
  def run(self):
    log.debug("Entering Algorithm SMALLEST")
    bin_collection = self.bins
    item_collection = self.items
    if not (bin_collection.count() > 0 and item_collection.count() > 0):
	 raise DistributionException("Please provide atleast one bin and item")
    def continue_fn( space, bin, item ):
	  if bin.occupied_space(space, item):
	     return False

	  m_y = bin.get_min_y_pos(cury)
          if space.x + (item.w > bin.w):
            """ try z now """
            space.z += item.d 
            space.x = 0
          else: 
            space.x += 1


          """ if curd fails and so does  curx """
          """ go up in height make sure y  """
          """ is at the proper juxtaposition """
          if space.z + item.d > bin.d:
            space.y += m_y.max_y
            space.x = m_y.min_x
            space.z = m_y.min_z
          """ if were at the top of the box """
          """ we cannot allocate any more space so we can move on """

          if int(cury + item.h) > bin.h:
	     return False
	  return True

    bin = bin_collection.next()
    while bin != None:
      log.info("Trying to allocate items for bin: {0}".format(bin.id))
      item_collection.reset()
      bin.start_time = time.time()
      item = item_collection.next()
      while item;
	item = item_collection.current()

	if not bin.can_fit( item ):
	    item_collection.next()
	    continue
	space = Space(x=0, y=0, z=0)
	can_continue = continue_fn(bin, space, item)
    
        """ if item.w > bin.w: """
        """ self.binner.add_lost(item) """
        while can_continue:
	    space.compute_next_sequence()
	    can_continue = continue_fn(bin, space, item)

	show_adding_box_log(space, item)

        slot = Slot.from_space_and_item(space, item)
        bin.append(slot)
      bin.end_time =time.time()
      bin = bin_collection.next()

    """
    to be the smallest bin we
    must allocate all space of the
    bin and be the smallest in size
    """
    smallest = find_smallest(item_collection, self.binner.packed_bins)
    self.binner.set_smallest(smallest)


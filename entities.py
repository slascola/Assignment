import point
import actions

class Background:
   def __init__(self, name, imgs):
      self.name = name
      self.imgs = imgs
      self.current_img = 0

   def get_images(self):
      return self.imgs
   
   def get_image(self):
      return self.imgs[self.current_img]
   def get_name(self):
      return self.name
   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs) 


class MinerNotFull:
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = 0
      self.animation_rate = animation_rate
      self.pending_actions = []
   
   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_rate(self):     
      return self.rate     

   def set_resource_count(self, n):
      self.resource_count = n

   def get_resource_count(self):
      return self.resource_count

   def get_resource_limit(self):
      return self.resource_limit

   def get_name(self):              
      return self.name

   def get_animation_rate(self):
      return self.animation_rate

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions

   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def entity_string(self):
      return ' '.join(['miner', self.name, str(self.position.x),
         str(self.position.y), str(self.resource_limit),
         str(self.rate), str(self.animation_rate)])


class MinerFull:
   def __init__(self, name, resource_limit, position, rate, imgs,
      animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = resource_limit
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self): 
      return self.imgs         

   def get_image(self):    
      return self.imgs[self.current_img] 

   def get_rate(self):
      return self.rate          

   def set_resource_count(self, n):          
      self.resource_count = n

   def get_resource_count(self):
      return self.resource_count

   def get_resource_limit(self):
      return self.resource_limit

   def get_name(self):
      return self.name 

   def get_animation_rate(self):
      return self.animation_rate

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions

   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

class Vein:
   def __init__(self, name, rate, position, imgs, resource_distance=1):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.resource_distance = resource_distance
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_rate(self):
      return self.rate        

   def get_resource_distance(self):
      return self.resource_distance

   def get_name(self): 
      return self.name   

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions
     
   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def entity_string(self):
      return ' '.join(['vein', self.name, str(self.position.x),
         str(self.position.y), str(self.rate),
         str(self.resource_distance)])


class Ore:
   def __init__(self, name, position, imgs, rate=5000):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.rate = rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_rate(self):
      return self.rate        

   def get_name(self): 
      return self.name   

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions
   
   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def self_string(self):
      return ' '.join(['ore', self.name, str(self.position.x),
         str(self.position.y), str(self.rate)])


class Blacksmith:
   def __init__(self, name, position, imgs, resource_limit, rate,
      resource_distance=1):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.resource_limit = resource_limit
      self.resource_count = 0
      self.rate = rate
      self.resource_distance = resource_distance
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_rate(self):
      return self.rate        

   def set_resource_count(self, n):              
      self.resource_count = n   

   def get_resource_count(self):
      return self.resource_count             

   def get_resource_limit(self):
      return self.resource_limit

   def get_resource_distance(self):
      return self.resource_distance

   def get_name(self): 
      return self.name     

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions
      
   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def entity_string(self):
      return ' '.join(['blacksmith', self.name, str(self.position.x),
         str(self.position.y), str(self.resource_limit),
         str(self.rate), str(self.resource_distance)])


class Obstacle:
   def __init__(self, name, position, imgs):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_name(self): 
      return self.name  

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def entity_string(self):
      return ' '.join(['obstacle', self.name, str(self.position.x),
         str(self.position.y)])

class OreBlob:
   def __init__(self, name, position, rate, imgs, animation_rate):
      self.name = name
      self.position = position
      self.rate = rate
      self.imgs = imgs
      self.current_img = 0
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_rate(self):
      return self.rate        

   def get_name(self): 
      return self.name             

   def get_animation_rate(self):
      return self.animation_rate

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions
      

   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)

   def blob_to_vein(self, world, vein): #blob class with blob_next position
      entity_pt = self.get_position()
      if not vein:
         return ([entity_pt], False)
      vein_pt = vein.get_position()
      if actions.adjacent(entity_pt, vein_pt):
         actions.remove_entity(world, vein)
         return ([vein_pt], True)
      else:
         new_pt = self.blob_next_position(world, entity_pt, vein_pt)
         old_entity = world.get_tile_occupant(new_pt)
         if isinstance(old_entity, Ore):
            actions.remove_entity(world, old_entity)
         return (world.move_entity(self,new_pt), False)

   def blob_next_position(self, world, entity_pt, dest_pt): #blobs with blob to vein
      horiz = actions.sign(dest_pt.x - entity_pt.x)
      new_pt = point.Point(entity_pt.x + horiz, entity_pt.y)

      if horiz == 0 or (world.is_occupied(new_pt) and
         not isinstance(world.get_tile_occupant(new_pt),
         Ore)):
         vert = actions.sign(dest_pt.y - entity_pt.y)
         new_pt = point.Point(entity_pt.x, entity_pt.y + vert)

         if vert == 0 or (world.is_occupied(new_pt) and
            not isinstance(world.get_tile_occupant(new_pt),
            Ore)):
            new_pt = point.Point(entity_pt.x, entity_pt.y)

      return new_pt

   def create_ore_blob_action(self, world, i_store): #oreblob class
      def action(current_ticks):
         self.remove_pending_action(action)

         entity_pt = self.get_position()
         vein = world.find_nearest(entity_pt, Vein)
         (tiles, found) = self.blob_to_vein(world, vein)

         next_time = current_ticks + self.get_rate()
         if found:
            quake = actions.create_quake(world, tiles[0], current_ticks, i_store)
            world.add_entity(quake)
            next_time = current_ticks + self.get_rate() * 2

         actions.schedule_action(self, world,
            self.create_ore_blob_action(world, i_store),
            next_time)

         return tiles
      return action

   def schedule_blob(self, world, ticks, i_store):
      actions.schedule_action(self,world, self.create_ore_blob_action(world, i_store),
         ticks + self.get_rate())
      actions.schedule_animation(self, world)


class Quake:
   def __init__(self, name, position, imgs, animation_rate):
      self.name = name
      self.position = position
      self.imgs = imgs
      self.current_img = 0
      self.animation_rate = animation_rate
      self.pending_actions = []

   def set_position(self, point):
      self.position = point

   def get_position(self):
      return self.position

   def get_images(self):
      return self.imgs

   def get_image(self):
      return self.imgs[self.current_img]

   def get_name(self): 
      return self.name             

   def get_animation_rate(self):
      return self.animation_rate

   def remove_pending_action(self, action):
      self.pending_actions.remove(action)

   def add_pending_action(self, action):
      self.pending_actions.append(action)

   def get_pending_actions(self):
      return self.pending_actions
      
   def clear_pending_actions(self):
      self.pending_actions = []

   def next_image(self):
      self.current_img = (self.current_img + 1) % len(self.imgs)



#def set_position(self, point):
 #  self.position = point

#def get_position(self):
 #  return self.position

#def get_images(self):
 #  return self.imgs

#def get_image(self):
 #  return self.imgs[self.current_img]

#def get_rate(self):
 #  return self.rate

#def set_resource_count(self, n):
 #  self.resource_count = n

#def get_resource_count(self):
 #  return self.resource_count

#def get_resource_limit(self):
 #  return self.resource_limit

#def get_resource_distance(self):
 #  return self.resource_distance

#def get_name(self):
#   return self.name

#def get_animation_rate(self):
 #  return self.animation_rate

#def remove_pending_action(self, action):
 #  if hasattr(self, "pending_actions"):
  #    self.pending_actions.remove(action)

#def add_pending_action(self, action):
 #  if hasattr(self, "pending_actions"):
  #    self.pending_actions.append(action)

#def get_pending_actions(self):
 #  if hasattr(self, "pending_actions"):
  #    return self.pending_actions
  # else:
   #   return []

#def clear_pending_actions(self):
 #  if hasattr(self, "pending_actions"):
  #    self.pending_actions = []

#def next_image(self):
 #  self.current_img = (self.current_img + 1) % len(self.imgs)


# This is a less than pleasant file format, but structured based on
# material covered in course.  Something like JSON would be a
# significant improvement.
#def self_string(self):
 #  if isinstance(self, MinerNotFull):
  #    return ' '.join(['miner', self.name, str(self.position.x),
   #      str(self.position.y), str(self.resource_limit),
    #     str(self.rate), str(self.animation_rate)])
   #elif isinstance(self, Vein):
    #  return ' '.join(['vein', self.name, str(self.position.x),
     #    str(self.position.y), str(self.rate),
      #   str(self.resource_distance)])
  # elif isinstance(self, Ore):
   #   return ' '.join(['ore', self.name, str(self.position.x),
    #     str(self.position.y), str(self.rate)])
   #elif isinstance(self, Blacksmith):
    #  return ' '.join(['blacksmith', self.name, str(self.position.x),
     #    str(self.position.y), str(self.resource_limit),
      #   str(self.rate), str(self.resource_distance)])
   #elif isinstance(self, Obstacle):
    #  return ' '.join(['obstacle', self.name, str(self.position.x),
     #    str(self.position.y)])
   #else:
    #  return 'unknown'


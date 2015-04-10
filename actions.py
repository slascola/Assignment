import entities
import worldmodel
import pygame
import math
import random
import point
import image_store

BLOB_RATE_SCALE = 4
BLOB_ANIMATION_RATE_SCALE = 50
BLOB_ANIMATION_MIN = 1
BLOB_ANIMATION_MAX = 3

ORE_CORRUPT_MIN = 20000
ORE_CORRUPT_MAX = 30000

QUAKE_STEPS = 10
QUAKE_DURATION = 1100
QUAKE_ANIMATION_RATE = 100

VEIN_SPAWN_DELAY = 500
VEIN_RATE_MIN = 8000
VEIN_RATE_MAX = 17000


def sign(x):
   if x < 0:
      return -1
   elif x > 0:
      return 1
   else:
      return 0


def adjacent(pt1, pt2): #function
   return ((pt1.x == pt2.x and abs(pt1.y - pt2.y) == 1) or
      (pt1.y == pt2.y and abs(pt1.x - pt2.x) == 1))


def next_position(world, entity_pt, dest_pt): #function
   horiz = sign(dest_pt.x - entity_pt.x)
   new_pt = point.Point(entity_pt.x + horiz, entity_pt.y)

   if horiz == 0 or worldmodel.is_occupied(world, new_pt):
      vert = sign(dest_pt.y - entity_pt.y)
      new_pt = point.Point(entity_pt.x, entity_pt.y + vert)

      if vert == 0 or worldmodel.is_occupied(world, new_pt):
         new_pt = point.Point(entity_pt.x, entity_pt.y)

   return new_pt


def blob_next_position(world, entity_pt, dest_pt): #blobs with blob to vein
   horiz = sign(dest_pt.x - entity_pt.x)
   new_pt = point.Point(entity_pt.x + horiz, entity_pt.y)

   if horiz == 0 or (worldmodel.is_occupied(world, new_pt) and
      not isinstance(world.get_tile_occupant(new_pt),
      entities.Ore)):
      vert = sign(dest_pt.y - entity_pt.y)
      new_pt = point.Point(entity_pt.x, entity_pt.y + vert)

      if vert == 0 or (worldmodel.is_occupied(world, new_pt) and
         not isinstance(world.get_tile_occupant(new_pt),
         entities.Ore)):
         new_pt = point.Point(entity_pt.x, entity_pt.y)

   return new_pt



def find_open_around(world, pt, distance): #function
   for dy in range(-distance, distance + 1):
      for dx in range(-distance, distance + 1):
         new_pt = point.Point(pt.x + dx, pt.y + dy)

         if (world.within_bounds(new_pt) and
            (not worldmodel.is_occupied(world, new_pt))):
            return new_pt

   return None



def create_animation_action(world, entity, repeat_count): #function
   def action(current_ticks):
      entity.remove_pending_action(action)

      entity.next_image()

      if repeat_count != 1:
         schedule_action(entity, world,
            create_animation_action(world, entity, max(repeat_count - 1, 0)),
            current_ticks + entity.get_animation_rate())

      return [entity.get_position()]
   return action


def remove_entity(entity, world): #function
   for action in entity.get_pending_actions():
      world.unschedule_action(action)
   entity.clear_pending_actions()
   world.remove_entity(entity)



def schedule_action(entity, world, action, time): #function
   entity.add_pending_action(action)
   world.schedule_action(action, time)


def schedule_animation(entity, world, repeat_count=0): #function
   schedule_action(entity, world,
      create_animation_action(world, entity, repeat_count),
      entity.get_animation_rate())


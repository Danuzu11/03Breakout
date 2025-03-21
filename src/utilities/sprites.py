from typing import List, Any

import settings
import pygame

# I used it for obtain sprites in dynamic form , only need coordinates , description of the sprite and sizes

def obtainImageSpriteSheet(description,new_width,new_heigth,flip,frame_index=0) -> pygame.Surface:
        #Obtain image and textures "cordinates" ins the spritesheet
        image = settings.TEXTURES[description]
        frames = settings.FRAMES[description]
        
        #Obtain image
        originalSprite = image.subsurface(frames[0][frame_index])
        
        #Resize Image
        newSprite = pygame.transform.scale(originalSprite,(new_width,new_heigth))
     
        # Decide if flip my image or not
        if flip == "Up":
            newSprite = pygame.transform.rotate(newSprite,-90)
            
        return newSprite  
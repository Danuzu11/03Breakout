import random
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class StickPower(PowerUp):
    """
    Power-up to add sticky power in the paddle.
    """ 

    def __init__(self, x: int, y: int) -> None:
        # RECUERDEN QUE EL TERCER PARAMETRO SELECCIONA EL TIPO DE BOLITA QUE RECIBIRA ES DECIR EL SPRITE DE LA BOLITA
        # EJEMPLO SI SELECCIONAN 1 SERA LA BOLITA QUE APARECE DE PRIMERO EN EL SPRITESHEET (REVISA LOS ASSET)
        super().__init__(x, y, 3)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        
        # AQUI COMO L EXPLIQUE A VERO PUEDEN USAR TODOS LOS PARAMETROS QUE USA PLAY STATE CON play_state.paddle o x cosa
        
        # ALGO QUE SE ME OCURRIO ES QUE SI DETECTA COLISION AGARRE LA PELOTA EN ESPECIFICO (RECUERDEN QUE HAY POSIBILIDAD DE VARIAS)
        # VUELVEN LA VELOCIDAD CERO Y SU VELOCIDAD EN X SERA LA MISMA QUE LA DEL PADDLE PORQUE LA PORQUERIA SE TIENE QUE MOVER CON EL PADDLE
        # AUNQUE TIENEN QUE SOLUCIONAR... QUE PASA SI DOS BOLITAS PEGAN EN EL MISMO LUGAR , PORQUE SI GERARDITO QUERIDO DIJO QUE SE PUEDEN PEGAR VARIAS :V
        # RECUERDA QUE SI AGREGAS DATOS NUEVOS EN LOS PARAMETROS DE PLAYSTATE O CUALQUIERA DEBES TENER CUIDADO PORQUE COMO BRINCAMOS DE ESTADO EN ESTADO PUES... HAY QUE PASARLOS
        # PORQUE SI PONE PAUSA LA PERSONA LOS PODERES Y RENDERIZADO DEBEN PERSISTIR ASI QUE TENGAN CUIDADO CON EL TEMA DE CAMBIO DE ESTADOS PARA MANTENER VARIABLES
        # NO ES DIFICIL SOLO MIREN DONDE CAMBIA DE ESTADO EN "change_state" Y AHI VEN QUE PASAN
        
        # COMO EXPLICACION BURDA DE ESTOS PODERES PARA AHORRARLES TRABAJO CREO xd ...
        # LA PORQUERIA DE PODERES FUNCIONA ASI.....
        
        # LA CARPETA "src/powerups" TIENE LO QUE CONTROLA LOS PODERES Y CUALES SERAN ESTOS
            # 1ER PUNTO.... CLASE BASE QUE GENERA BOLITAS DE PODER....
                # TENEMOS LA CLASE "PowerUp.py" ESTA MARDITA ES LA QUE ME AYUDA A GENERAR LAS BOLITAS QUE CAEN QUE DAN PODERES, COMO VEN DENTRO DE LA CLASE ESA JODA TIENE VELOCIDAD 
                # SI ESTA ACTIVO ETC... NO LE PAREN BOLAS NUNCA LA VAN A USAR SOLO PARA QUE SEPAN... PERO ESO SI SOLO UN PARAMETRO IMPORTANTE EL  self.active = False , DEJARLO EN SUS CLASES NUEVAS
                # ES IMPORTANTE PORQUE PONERLOS EN FALSE ES LO QUE HACE QUE LA BOLITA QUE NOS DA PODERES DESAPAREZCA
                
            # 2DO PUNTO.... NUEVOS PODERES....
                # COMO VIERON EN LA ANTERIOR SOLO GENERA LAS BOLITAS !! NO ASIGNA UN CSM DE PODER NADA , Y AQUI ES DONDE NOSOTROS DEBEMOS CREAR UNA CLASE NUEVA, COMO CannonBalls.py QUE CREE
                # PARA LOS CAÑONES EN ESTAS CLASES ES DONDE DECLARAREMOS BASICAMENTE "QUE HACE NUESTRO PODER BASE" PERO TENGAN CUIDADO NO LO HACE TODO PORQUE RECUERDEN QUE ESTO SOLO ES ASIGNADO
                # UNA SOLA VES , ES DECIR , CUANDO AGARRAMOS LA BOLITA OBTENEMOS UN PODER , LO QUE PONGAMOS AQUI DENTRO SERA LO QUE SE EJECUTE CUANDO AGRRE LA BOLITA , SOLO CUANDO LA AGARRE!!!
                # ASI QUE TENGAN CUIDADO CON EL TEMA DE PERSISTENCIA DE DATOS PA QUE NO SE COMPLIQUEN
                
                # NO SE SI LE AGARRAN LA IDEA PERO BASICAMENTE AQUI DECLARO LO QUE HARA EL JUEGO JUSTO!!! CUANDO AGARRE LA BOLITA NADA MAS!! 
                
                # POR ENDE CLARO AQUI... PUEDEN CAMBIAR LA VELOCIDAD A LA PELOTA A 0... PERO SOLO SE EJECUTARA ESTE CODIGO CUANDO AGARRE LA BOLITA DE PODER TONS NO SIRVE ESA MONDA!
                # LO QUE SE ME OCUREE AHORITA ES QUE LA IDEA ES QUE CREEN EN LA BOLITA UN PARAMETRO QUE DIGA "PEGADO" O "STICKY" 
                # Y EN PLAYSTATE CREEN UN PARAMETRO QUE INDIQUE QUE EL "PODER PEGADOR" ESTA ACTIVO Y METEN UNA CONDICIONAL PARA QUE SI ESTE PODER ESTA ACTIVO 
                # PASE LO DE QUE SU VELOCIDAD SE HAGA 0 Y DEMAS COSAS , SERIA UNA IDEA Y AQUI LO QUE PUEDES HACER ES QUE TODOS LOS PARAMETROS SE PONGAN COMO TRUE O ALGO ASI NO SE
                
        # ESO COMO EXPLICACION BASE DE PA QUE MARDICION SIRVEN ESTOS DOS TIPOS DE CLASES LAS DE PowerUp Y LAS NUEVAS QUE CREAREMOS QUE ES LO MAS LADILLA DE ENTENDER
        
        # LO DEMAS LO DEBEN HACER MODIFICANDO LOS ARCHIVOS DE PADDLE.PY , BALL.PY Y LOS STADOS DE PLAY PAUSE WIN SERVE etc
        
        # SI ES POSIBLE REUTILICEN LOS METODOS DE BALL , PARA CUANDO TENGAN QUE EXPULSAR TODAS LAS BOLITAS Y ASI
        
        # LO MAS LADILLA SON LO DE LOS PARAMETROS EN LOS ESTADOS PERO UNA VES QUE LE AGARRAN EL HILO ES COPIAR Y PEGAR
        
        # COMO ULTIMO RECUERDEN QUE DEBEN DECLARAR LA CLASE CUANDO CREEN UN PODER NUEVO EN "src/powerups/__init__.py" PARA QUE LES RECONOZCA LOS ARCHIVO DE POWERUPS COMO CLASES DIRECTO EN PLAYSTATE
        
        
        # AH Y RECUERDEN MODIFICAR EL ARRAY QUE HAY EN LOS PARAMETROS DE PLAYSTATE PARA AGREGAR MAS PODERES Y CREEN BOLITAS DISTINTAS 
            
        
        
        # play_state.cannon_active = True
        # play_state.cannon_ammo = 5
        # play_state.paddle.has_cannons = True
        self.active = False
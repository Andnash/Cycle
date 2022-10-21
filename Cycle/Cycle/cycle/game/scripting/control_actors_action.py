import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # P1 left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        # P1 right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # P1 up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)

        # P1 down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

        
        cycle = cast.get_first_actor("cycles")
        cycle.turn_head(self._direction)












class ControlActor_2_Action(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction_p2 = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        # P2 left
        if self._keyboard_service.is_key_down('j'):
            self._direction_p2 = Point(-constants.CELL_SIZE, 0)    

        # P2 right
        if self._keyboard_service.is_key_down('l'):
            self._direction_p2 = Point(constants.CELL_SIZE, 0)

        # P2 up
        if self._keyboard_service.is_key_down('i'):
            self._direction_p2 = Point(0, -constants.CELL_SIZE)

        # P2 down
        if self._keyboard_service.is_key_down('k'):
            self._direction_p2 = Point(0, constants.CELL_SIZE)
        
        cycle_2 = cast.get_first_actor("cycles2")
        cycle_2.turn_head(self._direction_p2)
        
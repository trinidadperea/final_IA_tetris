class Piece: 
    def __init__ (self,shape):
        self.shape = shape
        self.rotation = 0
        self.x = 3
        self.y = 0
        self.color = COLORS[shape]

    def get_current_shape(self):
        return SHAPES[self.shape][self.rotation]
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(SHAPES[self.shape])

SHAPES = {
    'I': [
        [  # rotación 0
            '.....',
            'OOOO.',
            '.....',
            '.....',
            '.....'
        ],
        [  # rotación 1
            '..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'
        ],
        [  # rotación 2
            '.....',
            '.....',
            'OOOO.',
            '.....',
            '.....'
        ],
        [  # rotación 3
            '..O..',
            '..O..',
            '..O..',
            '..O..',
            '.....'
        ]
    ],

    'O': [
        [  # no tiene rotacion
            '.....',
            '.....',
            '.OO..',
            '.OO..',
            '.....'
        ]
    ],

    'T': [
        [  #rotacion 0
            '.....',
            '..O..',
            '.OOO.',
            '.....',
            '.....'
        ],
        [  #rotacion 1
            '.....',
            '..O..',
            '..OO.',
            '..O..',
            '.....'
        ],
        [ #rotacion 2
            '.....',
            '.....',
            '.OOO.',
            '..O..',
            '.....'
        ],
        [  #rotacion 3
            '.....',
            '..O..',
            '.OO..',
            '..O..',
            '.....'
        ]
    ],

    'S': [
        [  #rotacion 0
            '.....',
            '..OO.',
            '.OO..',
            '.....',
            '.....'
        ],
        [  #rotacion 1
            '.....',
            '..O..',
            '..OO.',
            '...O.',
            '.....'
        ],
        [  #rotacion 2
            '.....',
            '..OO.',
            '.OO..',
            '.....',
            '.....'
        ],
        [  #rotacion 3
            '.....',
            '..O..',
            '..OO.',
            '...O.',
            '.....'
        ]
    ],

    'Z': [
        [  #rotacion 0
            '.....',
            '.OO..',
            '..OO.',
            '.....',
            '.....'
        ],
        [  #rotacion 1
            '.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....'
        ],
        [  #rotacion 2
            '.....',
            '.OO..',
            '..OO.',
            '.....',
            '.....'
        ],
        [  #rotacion 3
            '.....',
            '..O..',
            '.OO..',
            '.O...',
            '.....'
        ]
    ],

    'J': [
        [  #rotacion 0
            '.....',
            '.O...',
            '.OOO.',
            '.....',
            '.....'
        ],
        [  #rotacion 1
            '.....',
            '..OO.',
            '..O..',
            '..O..',
            '.....'
        ],
        [  #rotacion 2
            '.....',
            '.....',
            '.OOO.',
            '...O.',
            '.....'
        ],
        [  #rotacion 3
            '.....',
            '..O..',
            '..O..',
            '.OO..',
            '.....'
        ]
    ],

    'L': [
        [  #rotacion 0
            '.....',
            '...O.',
            '.OOO.',
            '.....',
            '.....'
        ],
        [  #rotacion 1
            '.....',
            '..O..',
            '..O..',
            '..OO.',
            '.....'
        ],
        [  #rotacion 2
            '.....',
            '.....',
            '.OOO.',
            '.O...',
            '.....'
        ],
        [  #rotacion 3
            '.....',
            '.OO..',
            '..O..',
            '..O..',
            '.....'
        ]
    ]
}

COLORS = {
    'I': (0, 255, 255),  # celeste
    'O': (255, 255, 0),  # amarillo
    'T': (128, 0, 128),  # violeta
    'S': (0, 255, 0),    # verde
    'Z': (255, 0, 0),    # rojo
    'J': (0, 0, 255),    # azul
    'L': (255, 165, 0)   # naranja
}


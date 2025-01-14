class Cour:
    def __init__(self, week, name, start_hour, end_hour):
        self.week = week
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour

monday = [
    Cour(
        'a&b',
        'Philosophie',
        '08:00:00',
        '09:30:00'
    ),
    Cour(
        'a',
        'Informatique',
        '10:00:00',
        '11:30:00'
    ),
    Cour(
        'b',
        'Informatique',
        '11:30:00',
        '13:00:00'
    )
]

tuesday = [
    Cour(
        'a&b',
        'Histoire',
        '08:30:00',
        '10:00:00'
    ),
    Cour(
        'a&b',
        'Mathématiques',
        '10:30:00',
        '12:00:00'
    ),
    Cour(
        'a',
        'Physique',
        '13:00:00',
        '14:30:00'
    ),
    Cour(
        'b',
        'Chimie',
        '13:00:00',
        '14:30:00'
    ),
    Cour(
        'a&b',
        'Sport',
        '15:00:00',
        '16:30:00'
    )
]

wensday = [
    Cour(
        'a&b',
        'Géographie',
        '08:00:00',
        '09:30:00'
    ),
    Cour(
        'a',
        'Sciences Sociales',
        '10:00:00',
        '11:30:00'
    ),
    Cour(
        'b',
        'Économie',
        '10:00:00',
        '11:30:00'
    ),
    Cour(
        'a&b',
        'Musique',
        '12:00:00',
        '13:30:00'
    )
]

thursday = [
    Cour(
        'a&b',
        'Anglais',
        '08:30:00',
        '10:00:00'
    ),
    Cour(
        'a',
        'Arts Plastiques',
        '10:30:00',
        '12:00:00'
    ),
    Cour(
        'b',
        'Technologie',
        '10:30:00',
        '12:00:00'
    ),
    Cour(
        'a&b',
        'Mathématiques Avancées',
        '13:30:00',
        '15:00:00'
    )
]

friday = [
    Cour(
        'a&b',
        'Biologie',
        '08:00:00',
        '09:30:00'
    ),
    Cour(
        'a',
        'Physique-Chimie',
        '10:00:00',
        '11:30:00'
    ),
    Cour(
        'b',
        'Sciences de la Terre',
        '10:00:00',
        '11:30:00'
    ),
    Cour(
        'a&b',
        'Français',
        '13:00:00',
        '14:30:00'
    ),
    Cour(
        'a&b',
        'Histoire de l'Art',
        '15:00:00',
        '16:30:00'
    )
]

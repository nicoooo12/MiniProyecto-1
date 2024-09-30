from buzzer import play, setup

def init():
  melody = [
    'G4','B4','D5',
    '0','F4','F5','E5','DS5',
    'D5','F4','E4','DS4',
    'D4','C4','B2','C4',

    'G4','B4','D5',
    '0','G4','B4','G4',
    'D5','F4','E4','C4',
    'D4','B3','C4','D4',

    'G4','B4','D5',
    '0','F4','F5','E5','DS5',
    'D5','F4','E4','DS4',
    'D4','C4','B3','C4',

    'G4','B4','D5',
    '0','F5','E5','F5',
    'G5','AS5','G5',
  ]
  tempo = [
    1.5,1/2,2,
    1.5,1/2,1.5,1/4,1/4,
    2,1.5,1/4,1/4,
    2,8/12,8/12,8/12,
    1.5,1/2,2,
    2,8/12,8/12,8/12,
    2,8/12,8/12,8/12,
    30/12,1/2,1/2,1/2,
    1.5,1/2,2,
    1.5,1/2,1.5,1/4,1/4,
    2,1.5,1/4,1/4,
    2,8/12,8/12,8/12,
    1.5,1/2,2,
    2,8/12,8/12,8/12,
    1.5,1/2,4
  ]
  
  setup()
  play(melody, tempo, 133)

if __name__ == '__main__':
    init()

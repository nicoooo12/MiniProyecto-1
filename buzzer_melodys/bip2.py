from buzzer import play, setup

def init():
  melody = [
    'G4',0, 'G4'
  ]
  tempo = [
    0.1,0.1, 0.2
  ]
  
  setup()
  play(melody, tempo, 133)

if __name__ == '__main__':
    init()
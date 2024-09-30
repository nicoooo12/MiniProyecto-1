from buzzer import play, setup

def init():
  melody = [
    'A5',0,'A5',0,'A5',0, 'E6'
  ]
  tempo = [
    1.5,0.5, 1.5,0.5, 1.5,0.5, 2
  ]
  
  setup()
  play(melody, tempo, 133)

if __name__ == '__main__':
    init()
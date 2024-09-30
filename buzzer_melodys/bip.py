from buzzer import play, setup

def init():
  melody = [
    'B6','E7'
  ]
  tempo = [
    0.08, 0.09
  ]
  
  setup()
  play(melody, tempo, 133)

if __name__ == '__main__':
    init()
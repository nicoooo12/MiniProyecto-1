def dyInit():
    dy = 0
    while True:
      txt = input('*')
      if txt != '':
          dy += 1  
          break
      else:
          dy += 1  
    print ('\n'*dy)
    return dy

def PrintMenu(item, select, title, dy=10):
    print('\n'* 5)
    l = len(item)
    margin = int((dy - (5 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))
    print(f'[  {title}  ]\n')
    for i in range(len(item)):
        print(f'{">" if i == select else " "} {item[i]}')
    
    print('\n'* mb)
    print('=' * 46)

def PrintGraph(item, l=1, dy=10):
    print('\n'* 5)
    margin = int((dy - (3 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))

    print(item)

    print('\n'* mb)
    print('=' * 46)
    
def PrintTable(title, item, encabezado, num, dy=10):
    print('\n'* 5)
    l = len(item)
    margin = int((dy - (8 + l)) / 2)
    mt = margin if dy%2 == 0 else (margin +1)
    mb = margin
    print('=' * 20, 'Menu', '='*20)
    print('\n'* (mt-1))
    print(f'[  {title}  ]\n')
    
    print(f'{(" " if num else "")}  ', end='')
    for i in encabezado:
        print(f'{i:10}', end='')
    print('\n')
    for y in range(len(item)):
        for x in range(len(item[y])): 
            print(f'{((y+1)if num else "")if x ==0 else ""}  {item[y][x]:7}', end='')
        print('',end='\n')
    print('\n'* mb)
    print('=' * 46)

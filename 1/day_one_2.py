#########################################################################
##                                                                     ##
##                   AoC day 1 part 2 - 22/12/23                       ##
##                                                                     ##
#########################################################################

w_2_n = {3: {'one':1, 'two':2, 'six':6},
            4: {'four':4, 'five':5, 'nine':9, 'zero':0},
            5: {'three':3, 'seven':7, 'eight':8}}

def leer_archivo(nombre):
  archivo = open(nombre, "r")
  lineas = archivo.readlines()
  archivo.close()
  return lineas

def mapeo(numero):
  n = len(numero)
  try:
    return w_2_n[n][numero]
  except:
    return -1   

def extraigo_nums(linea, DEBUG=False):
  nums = []
  aux = ''
  i, j = 0, 0
  while j < len(linea):
    if DEBUG: print("DEBUG: j = ", j)
    aux = ''
    if not linea[j].isdigit():
        i = j
        while i < len(linea):
          if DEBUG: print("------ DEBUG: i = ", i)
          aux += linea[i]
          if DEBUG: print(f"\t i = {i} aux = {aux}")
          if mapeo(aux) > -1: 
            nums.append(str(mapeo(aux)))
            if DEBUG: print(f"\t\t Encontre un numero de letras: {mapeo(aux)}") 
            j = i-1 
            break
          i += 1
    elif linea[j].isdigit():
      if DEBUG: print(f"\t\t Encontre un numero: {linea[j]}") 
      nums.append(linea[j])
      i += 1
    j += 1
         
  if len(nums) > 1: 
    return int(nums[0] + nums[-1])
  else:
    return int(nums[0]*2)

if __name__ == '__main__':
  archivo = input('Nombre del archivo: ')
  lineas = leer_archivo(archivo)
  #lineas="two1nine"
  codigo = 0  
  for linea in lineas:
    codigo += extraigo_nums(linea)
    print(extraigo_nums(linea))
  #codigo += extraigo_nums(lineas)
  print(codigo)
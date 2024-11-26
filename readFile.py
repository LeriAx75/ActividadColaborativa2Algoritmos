def read_file(file_path):
  matrix=[]
  with open(file_path, 'r') as file:
    input=file.read().strip()
    for linea in input.split('\n'):
      if linea.strip():
        matrix.append(list(map(int,linea.split(' '))))
  return matrix
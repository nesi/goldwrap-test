import os      

def find_path_for_file(filename):
  for root, dirs, files in os.walk('.'):
    for file in files:
      if file == filename:
        return os.path.join(root, file)

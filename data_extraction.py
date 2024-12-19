import os

def files_basic():
    return [{'name': f, 'size': os.path.getsize(f)} for f in os.listdir() if os.path.isfile(f)]

def files_advanced(path=None):
    results = []
    for root, _, files in os.walk(path or os.getcwd()):
        results.extend({'name': f, 'path': os.path.join(root, f), 'size': os.path.getsize(os.path.join(root, f))} 
                      for f in files)
    return results

def files_complex(path=None):
    def scan_dir(dir_path):
        result = {'files': {}, 'dirs': {}}
        for entry in os.scandir(dir_path):
            if entry.is_file():
                result['files'][entry.name] = {'size': entry.stat().st_size}
            elif entry.is_dir():
                result['dirs'][entry.name] = scan_dir(entry.path)
        return result
    return scan_dir(path or os.getcwd())

# Test the function with your path
results = files_advanced("/home/engineer/Desktop/projects")
print(results)
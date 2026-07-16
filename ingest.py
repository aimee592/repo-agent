import os
def load_repository(repo_path) :
    output = []
    dirs[:] = [
        d for d in dirs
        if d not in {".git", "__pycache__", "venv", "node_modules"}
    ]
    for root, dirs, files in os.walk(repo_path) :
      
        for file in files: 
            if file.endswith(".py") :
                path = os.path.join(root, file)
                
                try:
                    with open (path, "r", encoding="utf-8") as f:
                            
                        text = f.read()
                except Exception:
                    continue
                
                output.append({
                    "path" : path,
                    "content" : text
                })
    return output

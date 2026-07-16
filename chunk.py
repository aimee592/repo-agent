def chunk_repository(files, chunk_size = 1000, overlap = 200) :
    output = []
    for file in files:
        c_id = 0
        start = 0
        text = file["content"]
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            output.append({
                "path" : file["path"],
                "chunk_id" : c_id,
                "text" : chunk
            })
            step = chunk_size - overlap
            start += step
            c_id += 1
    return output
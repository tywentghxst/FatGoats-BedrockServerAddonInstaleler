import zipfile, os, json

def handle_upload(file):
    filename = file.filename
    if not filename.endswith((".mcaddon", ".mcpack")):
        return {"error": "Invalid file format"}
    save_path = os.path.join("/packs", filename)
    file.save(save_path)
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        extract_path = save_path.replace(".mcaddon", "").replace(".mcpack", "")
        zip_ref.extractall(extract_path)
    return {"status": "uploaded", "path": extract_path}

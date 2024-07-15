import magic

def detect_file_type(file_path):
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    
    if file_type == 'application/pdf':
        return 'PDF'
    elif file_type == 'application/msword':
        return 'DOC'
    elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return 'DOCX'
    else:
        return 'Unknown'

# # Exemple d'utilisation
# file_path = 'CV - Sami CHAOUCH - WB EN.docx'
# file_type = detect_file_type(file_path)

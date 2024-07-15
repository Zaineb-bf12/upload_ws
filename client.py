import json
import base64
import websockets
import asyncio

async def send_pdf():
    uri = "ws://127.0.0.1:8000/ws/pdf/"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwNzgyMTIyLCJpYXQiOjE3MjA2OTU3MjIsImp0aSI6IjQ2ODgzZDk2MTM0ZDRlNmNhMTAyOWZlOTE3NmYyOTZhIiwidXNlcl9pZCI6MX0.WAgnxIT7-rJPW3WHdnk7VExLgJqrUdd9l_qXg33LhRg"  # Remplacez par votre token si nécessaire

    async with websockets.connect(uri,ping_interval=60, ping_timeout=60, extra_headers={'Authorization': f'Bearer {token}'}) as websocket:
        # Ouvrir et lire le fichier PDF
        with open("CV - Sami CHAOUCH - WB EN.docx", "rb") as pdf_file:
            pdf_data = pdf_file.read()

        # Encoder en base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
        
        # Préparer les données JSON
        data = {
            "file_base64": pdf_base64,
            "file_name": "filename.pdf"
        }

        # Envoyer les données JSON
        await websocket.send(json.dumps(data))

        # Recevoir la réponse
        response = await websocket.recv()
        print("Received response:", response)

asyncio.run(send_pdf())
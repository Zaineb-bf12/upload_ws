# websocket/consumers.py
import json
import base64
import os
import tempfile
from channels.generic.websocket import AsyncWebsocketConsumer
from websocket.utils.file_type import detect_file_type
from websocket.utils.pdf_text import extract_text_from_pdf
from websocket.utils.docx_text import extract_text_and_tables_from_docx
from websocket.utils.text_json import extract_and_combine

class FileProcessorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        try:
            if text_data:
                request = json.loads(text_data)
                file_base64 = request.get("file_base64")
                file_name = request.get("file_name")

                # Debugging: Print out the received data
                print(f"Received file_base64: {file_base64}")
                print(f"Received file_name: {file_name}")

                if file_base64 and file_name:
                    # Save the base64 file to a temporary file
                    file_path = await self.save_base64_to_file(file_base64, file_name)
                    print(f"Received file_path: {file_path}")

                    if file_path:
                        response = await self.process_file(file_path)
                        # Clean up the temporary file
                        os.remove(file_path)
                    else:
                        response = {"error": "Failed to save file from base64"}

                else:
                    response = {"error": "No file base64 or file name provided"}

                await self.send(text_data=json.dumps(response))

        except json.JSONDecodeError:
            error_message = {"error": "Invalid JSON format"}
            await self.send(text_data=json.dumps(error_message))
        except Exception as e:
            error_message = {"error": f"An error occurred: {str(e)}"}
            await self.send(text_data=json.dumps(error_message))

    async def save_base64_to_file(self, file_base64, file_name):
        try:
            # Decode the base64 file content
            file_data = base64.b64decode(file_base64)
            
            # Create a temporary file with the appropriate suffix
            suffix = os.path.splitext(file_name)[1]
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
            temp_file.write(file_data)
            temp_file.close()

            return temp_file.name
        except Exception as e:
            print(f"Error saving base64 file: {e}")
            return None

    async def process_file(self, file_path):
        try:
            if not os.path.exists(file_path):
                return {"error": f"File not found: {file_path}"}

            file_type = detect_file_type(file_path)

            if file_type == 'DOCX':
                text = extract_text_and_tables_from_docx(file_path)
            elif file_type == 'PDF':
                print("**********")
                text = extract_text_from_pdf(file_path)
            else:
                return {"error": "Unsupported file type"}

            combined_text = extract_and_combine(text)
            print('_____________________')
            return {"text": combined_text}

        except Exception as e:
            return {"error": str(e)}

from docx import Document
def extract_text_and_tables_from_docx(file_path):
    doc = Document(file_path)
    full_text = []
    
    for element in doc.element.body:
        if element.tag.endswith('p'):  # Paragraph
            para = element
            full_text.append(para.text)
        elif element.tag.endswith('tbl'):  # Table
            table = element
            for row in table.findall('.//w:tr', namespaces=doc.element.nsmap):
                row_text = []
                for cell in row.findall('.//w:tc', namespaces=doc.element.nsmap):
                    cell_text = ''.join(cell.itertext())
                    row_text.append(cell_text.strip())
                full_text.append('\t'.join(row_text))
            full_text.append('')  # Add a blank line after the table

    return '\n'.join(full_text)
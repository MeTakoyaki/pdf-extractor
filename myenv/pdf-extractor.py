import argparse
import os
import fitz  # PyMuPDF
from odf.opendocument import OpenDocumentText
from odf.text import P
from tqdm import tqdm

def extract_pdf_to_odt(pdf_path, output_file):
    os.makedirs("output-ekstraksi", exist_ok=True)
    output_path = os.path.join("output-ekstraksi", output_file)
    doc = fitz.open(pdf_path)
    
    new_doc = OpenDocumentText()
    
    for page in tqdm(doc, desc="Mengekstrak PDF", unit="halaman"):
        text = page.get_text("text")
        paragraphs = text.split("\n\n")  # Pisahkan berdasarkan paragraf kosong
        
        for paragraph in paragraphs:
            if paragraph.strip():  # Pastikan bukan paragraf kosong
                new_doc.text.addElement(P(text=paragraph.strip()))
    
    new_doc.save(output_path)
    print(f"Ekstraksi selesai! Hasil disimpan di {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ekstrak teks dari PDF dan simpan dalam ODT.")
    parser.add_argument("input_pdf", help="Nama file PDF yang akan diekstrak")
    parser.add_argument("output_odt", help="Nama file output dalam format ODT")
    
    args = parser.parse_args()
    extract_pdf_to_odt(args.input_pdf, args.output_odt)

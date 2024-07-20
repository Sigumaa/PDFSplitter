import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, pages_one, pages_two):
    input_pdf = PdfReader(input_pdf_path)

    output_one = PdfWriter()
    output_two = PdfWriter()

    for page_num in pages_one:
        output_one.add_page(input_pdf.pages[page_num - 1])

    for page_num in pages_two:
        output_two.add_page(input_pdf.pages[page_num - 1])

    with open("output_one.pdf", "wb") as out_file:
        output_one.write(out_file)

    with open("output_two.pdf", "wb") as out_file:
        output_two.write(out_file)

def parse_args():
    parser = argparse.ArgumentParser(description='Split a PDF into two based on specified page numbers.')
    parser.add_argument('input_pdf', help='The input PDF file')
    parser.add_argument('--one', required=True, help='Comma-separated list of pages for the first output PDF')
    parser.add_argument('--two', required=True, help='Comma-separated list of pages for the second output PDF')
    return parser.parse_args()

def main():
    args = parse_args()
    pages_one = [int(x) for x in args.one.split(',')]
    pages_two = [int(x) for x in args.two.split(',')]
    split_pdf(args.input_pdf, pages_one, pages_two)

if __name__ == "__main__":
    main()

import PyPDF2
import click
from pathlib import Path


@click.command()
@click.option("--input_dir", type=click.Path(file_okay=False, dir_okay=True, path_type=Path), default="./data", help="The path of the directory that stores the input PDF files")
@click.option("--output_path", type=click.Path(file_okay=True, dir_okay=False, path_type=Path), default="./output.pdf", help="The path of the file that will store the PDF files")
def main(input_dir: Path, output_path: Path):
    # Get all PDF files in the input folder
    pdf_paths = sorted([f for f in input_dir.glob("**/*.pdf")])
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Add each PDF to the merger in order
    for pdf_path in pdf_paths:
        pdf_merger.append(pdf_path)

    # Write the merged PDF to the output file
    with output_path.open("wb") as output_file:
        pdf_merger.write(output_file)


if __name__ == "__main__":
    main()

## INSTALL THE REQUIRED PACKAGES ##
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def generate_cv(input_folder, language):
    # Load CV from PDF
    cv_pdf_path = os.path.join(input_folder, "cv.pdf")
    cv_text = extract_text_from_pdf(cv_pdf_path)

    # Load additional information file
    extra_info_path = os.path.join(input_folder, "extra_info.txt")
    extra_info = read_text_file(extra_info_path)

    # Tailor CV based on additional information
    tailored_cv = tailor_cv(cv_text, extra_info)

    # Translate CV if necessary
    if language == "German":
        tailored_cv = translate_to_german(tailored_cv)

    return tailored_cv


def generate_cover_letter(input_folder, job_post_path, language):
    # Load job post
    job_post = read_text_file(job_post_path)

    # Generate cover letter based on job post
    cover_letter = generate_cover_letter_from_job_post(job_post)

    # Translate cover letter if necessary
    if language == "German":
        cover_letter = translate_to_german(cover_letter)

    return cover_letter


def save_document(document, output_path):
    document.save(output_path)


def main():
    # Input folder
    input_folder = input("Enter the path to the input folder: ")

    # Language selection
    language = input("Select language (English or German): ").strip()

    # Job post file path
    job_post_path = os.path.join(input_folder, "job_post.txt")

    # Generate tailored CV
    tailored_cv = generate_cv(input_folder, language)
    cv_output_path = os.path.join(input_folder, f"tailored_cv_{language.lower()}.docx")
    save_document(tailored_cv, cv_output_path)
    print(f"Tailored CV generated: {cv_output_path}")

    # Generate cover letter
    cover_letter = generate_cover_letter(input_folder, job_post_path, language)
    cover_letter_output_path = os.path.join(
        input_folder, f"cover_letter_{language.lower()}.docx"
    )
    save_document(cover_letter, cover_letter_output_path)
    print(f"Cover letter generated: {cover_letter_output_path}")


if __name__ == "__main__":
    main()

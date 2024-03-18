FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install build-essential cmake wget -y
RUN apt-get update -y
RUN apt-get install python-is-python3
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip install my-tex-lib==0.1.2
RUN yes | apt-get install texlive-latex-base
RUN pip install pdflatex
RUN mkdir work

WORKDIR /work
COPY tex_lib/tex_lib/images images
COPY generate_tex_and_pdf.py generate_pdf.py
RUN python generate_pdf.py
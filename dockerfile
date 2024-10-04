FROM continuumio/miniconda3:latest

WORKDIR /code

RUN echo 'CONDA VERSION INSTALLED --- ' \
    && conda --version

COPY ./environment.yml /code/environment.yml

RUN conda env create -f /code/environment.yml

COPY ./app /code/app

# CMD ["conda", "run", "-n", "farm", "uvicorn", "-u", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

CMD ["bash", "-c", "source activate farm && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]

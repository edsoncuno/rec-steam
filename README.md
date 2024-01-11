# REC Steam

Motor de recomendacion para Steam

```bash
docker run -it -p 8000:8000 -v $PWD:/usr/src/app “fastapi_entorno“
```

## Desarrollo

Para utilizar el entorno de desarrollo se necesita:

```bash
uvicorn main:app --reload
```

Los paquetes que se tiene que instalar para realizar el proceso de ETL en los notebook y desarrollo del backend:

```bash
pip install seaborn ipykernel pyarrow fastparquet fastapi uvicorn
```

Tambien se debe instalar la libreria de NLP utilizada en este proyecto

https://textblob.readthedocs.io/en/dev/

```bash
pip install textblob
# en linux
python3 -m textblob.download_corpora
# en windows
python -m textblob.download_corpora
```
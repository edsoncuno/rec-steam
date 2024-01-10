```bash
docker run -it -p 8000:8000 -v $PWD:/usr/src/app “fastapi_entorno“
```

```bash
uvicorn main:app --reload
```

```bash
docker start -a “fastapi_entorno“
```

Los paquetes que se tiene que instalar para realizar el proceso de ETL en los notebook, son:

```bash
pip install numpy pandas matplotlib seaborn
# librerias para usar el formato parquet
pip install pyarrow fastparquet
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
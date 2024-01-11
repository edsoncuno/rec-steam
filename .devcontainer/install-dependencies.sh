echo "Installing Developer Requirements"

echo "================================="

pip install seaborn ipykernel pyarrow fastparquet fastapi uvicorn textblob pandas

python -m textblob.download_corpora
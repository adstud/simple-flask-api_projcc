from google.cloud import bigquery
import os

def load_data_to_bigquery():
    client = bigquery.Client()
    dataset_id = os.getenv("GOOGLE_CLOUD_PROJECT") + ".books"
    table_id = dataset_id + ".books"
    uri = "gs://books/books.csv"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, autodetect=True
    )

    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
    load_job.result()
    print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}")

if __name__ == "__main__":
    load_data_to_bigquery()

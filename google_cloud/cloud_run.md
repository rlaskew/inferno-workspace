Some notes here


PROJECT_ID="$(gcloud config get-value project)"
gcloud config set run/region us-central1

docker pull quay.io/richardaskewredhat/sample-flask:april2022
docker tag quay.io/richardaskewredhat/sample-flask:april2022 gcr.io/${PROJECT_ID}/sample-flask:april2022
docker push gcr.io/${PROJECT_ID}/sample-flask:april2022

gcloud run deploy hello --image=gcr.io/${PROJECT_ID}/sample-flask:april2022 --allow-unauthenticated --port=5000 --region=us-central1 --project=${PROJECT_ID}

gcloud run deploy demo-flask --image=gcr.io/${PROJECT_ID}/sample-flask:april2022 --allow-unauthenticated

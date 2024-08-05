
echo "BUILD START"

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

echo "BUID END"
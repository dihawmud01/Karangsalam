 echo "BUILD START"
 python3.9 -m pip install -r requirements.txt

 echo "Make Migration..."
 python3.9 run.py makemigrations --noinput
 python3.9 run.py migrate --noinput

  echo "Collect  Statitic"
 python3.9 run.py collectstatic --noinput --clear

 echo "BUILD END"
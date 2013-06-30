now=$(date +"%m.%d.%Y")
python ccp/manage.py modelscount 2> "$now.dat"
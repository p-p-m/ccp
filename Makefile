test:
	python ccp/manage.py test
syncdb:
	python ccp/manage.py syncdb 
migrate:
	python ccp/manage.py migrate --noinput
run:
	python ccp/manage.py runserver

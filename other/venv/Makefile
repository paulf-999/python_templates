deps:
	$(info [+] Download the relevant dependencies)
	pip3 install virtualenv
	virtualenv -p python3 venv
	. venv/bin/activate

install:
	$(info [+] Install any required python / airflow libraries)
	pip3 install apache-airflow==${AIRFLOW_VERSION}
	pip3 install snowflake-connector-python==2.4.1
	pip3 install snowflake-sqlalchemy==1.2.4
	#pip3 install markdown
	#pip3 install wtforms==2.3.3
	#pip3 install SQLAlchemy==1.3.24
	#pip3 install Flask-SQLAlchemy==2.4.4

end:
	deactivate

clean:

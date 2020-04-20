
# Useful commands

Don't forget to activate the virutal env:

`source ~/.local/share/virtualenvs/react-django-cb-I2WWBHpH/bin/activate`
 and then to run the shell:
 
`python manage.py shell`

# Reset and make migrations

To reset migrations:

`python manage.py migrate chatterbox zero`

To make migrations:
`python manage.py makemigrations`

# Seed the db with reference data

From a virgin db install:
`python manage.py migrate` to run migrations
`python manage.py loaddata courses` to seed course data
`python manage.py loaddata organisations` to seed organisation data

# See db with some test data (students)

`python manage.py import_students x` will import student data for organisation 1 (AEKI)

This command will empty all AEKI students first, then repopulate using the `students_AEKI.csv` file as the source data

# Coverage report

`coverage run --source='.' manage.py test`
`coverage html` or `coverage report`

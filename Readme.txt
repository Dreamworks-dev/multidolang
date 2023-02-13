
1. Create your virtual environment.
2. Then activate this environment.
3. Navigate to "domain_language" folder.
4. Run command "pip install -r requirements.txt"
   And "py manage.py migrate"
   This will generate database file named "db.sqlite3".
5. Finally, run "py manage.py createsuperuser" and "py manage.py runserver"

In your browser, navigate to the link:
	"en.superproject.localhost"
	"de.superproject.localhost"
	"fr.superproject.localhost"
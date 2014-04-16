#!/bin/sh

#Star the server
python manage.py runserver
#Create dabatabases once configured the file rents/settings.py
python manage.py syncdb
#Do this due to this problem with NoSQL Databases https://gist.github.com/ielshareef/2986459 , http://stackoverflow.com/questions/8819456/django-mongodb-engine-error-when-running-tellsiteid
site_id=$(python site.py)
echo 'SITE ID IS:'
echo $site_id
#Add the new site ID to settings.py
sed -i 's/SITE_ID = 1/SITE_ID = '\'$site_id\''/g' rents/settings.py

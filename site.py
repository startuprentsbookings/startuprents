#from django.core.management import setup_environ

#from rents import settings

#setup_environ(settings)

#!/usr/bin/env python
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rents.settings")

    from django.contrib.sites.models import Site

    s = Site()
    s.save()
    site_id = s.id
    print(site_id)



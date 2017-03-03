# GEVENT Example with Github API
This program is used to fetch the organization's top repos and its corresponding top contributors.

Python is synchronous. Fetching multiple API requests will make the user to wait for a long time. There comes the Gevent to rescue. It uses luightweight execution units *greenlet*.

###Instructions

```pip install -r requirements.txt
python gitapi.py```

Due to github ratelimit, an IP address can make only sixty requests per hour. Please modify the code if you need to hit more than that.

################
Django IP logger
################
Django application for saving IP adresses visiting a web application.

=====
Intro
=====
As your web application scales, you will often encounter different reasons to keep track of IP Addresses. Perhaps, you just rolled out an Advert application and need to track visits and interactions in the back-end; perhaps, an 'evil' IP address continously pesters your endpoints without provocation and you'd like to implement a blacklist; better still, you need to track visitors across web pages on a 'IP' basis rather than just sessions.

Or perhaps, you have this biting need to have fun and fill production DBs with IP adresses whether you need it or not.

This application is a quite simple and effective solution to that.

^^^^^^^^^^
How to do?
^^^^^^^^^^
It's quite simple to use. Install with:
``pip install django-ip-logger``

Next step is to  add `ip_logger` to your INSTALLED_APPS like so::

    INSTALLED_APPS = [
        #... apps I don't care about here
        'ip_logger',
    ]


Next is to add `ip_logger.middleware.LogIPMiddleware` to the top of the list of MIDDLEWARES:

    MIDDLEWARE = [
        'ip_logger.middleware.LogIPMiddleware',
        # ... stuffs that's not my business
    ]

^^^^^^^^
Working?
^^^^^^^^
To test it's working, visit a random URL on your webapp and check that your IP has been added to the list.

----
FAQs
----
1. Why don't you save other stuffs like requests, responses, response time, queries, url paths and the sorts?
    For the sake of generalization and to prevent bloating, I've decided to save only IPs, first visit and recent visit time. This is to ensure your DB is not populated with lots of rows for the sake of 'robust-ness'. Most web apps won't need it. If you do, implement it yourself, you've got the `IPAdress` model there for you.

2. Do I need additional configurations?
    No, boss... You don't.

3. Nothing's working, I've tried every possible option
    Quit the project, it's not worth it.

4. This stuff is too simple, why implement it?
    Since you didn't implement it, I did.

5. Why did you choose this name for the package?
    Don't question my decisions. It took me 3 days to make this decision.

6. Is this package needed?
    Depends.

-----
Bugs?
-----
Raise an issue, I'll check it out.

--------------
Contributions?
--------------
Oh well... Make a PR

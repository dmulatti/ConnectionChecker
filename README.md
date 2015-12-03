ConnectionChecker
----
----
This is a script written in python that pings my home IP every 60 seconds to 
see if it's still alive. If my connection goes down, it'll send me an email and
keep trying to ping my home ip until it comes back up, at which point it'll 
send me another email.

This is run in the background on an external web server. The DNS entry pointing
to my home IP is kept updated using dynamic DNS.

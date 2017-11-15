# EONS


<pre><code>
Install the following to use EONS:
pip install flask
pip install bs4
pip install --upgrade watson-developer-cloud
pip install requests
pip install polyline
</code></pre>


##### How we built it
We used various APIs, including IBM Watson and various Google Map APIs to create the routes. The site is built with python and and utilizes javascript for many of the map related aspects.


##### Inspiration
Being New Yorkers, we spend a lot of our lives walking from place to place. Although NYC is generally a safe city, there are certain areas of NYC where one may feel unsafe. We wanted to create an app that would help New Yorkers feel safe wherever they are traveling. Jane Jacob's developed a theory that users feel most safe when there are other people present. Not only do they FEEL safe, but statistically, they are less likely to be harmed with more people present. Using this theory, we decided to create an app that would give users the optimal route for safe travels.

##### What it does
We leveraged NYC's open data live camera information and IBM Watson's facial recognition to determine the safest route. EONS is an app that calculates the safest route from one point to another. It does this by using camera information from cameras located throughout New York City. Using the cameras, EONS tracks the number of pedestrians present on all possible routes. Statistically, the safest route will be the one with the most people present, according to Jane Jacob's Eyes on the Street Theory. EONS uses IBM Watsons API to use facial recognition to count the number of people present when fed information from the cameras. EONS analyzes Watson's response to provide the path that is more likely to have more people.


##### Accomplishments that we're proud of
We are most proud of leveraging NYC's open data live camera information and IBM Watson's facial recognition to determine the safest route. We are most proud of our efficient use of the Google and Watson APIs and being able to successfully integrate them into our application.


Submittin Your Work

* Try to get your code running on your VM
  I was able to finally get flaskr working on my vm:
  http://block647052-gfz.blueboxgrid.com

* Add a README.txt file that discusses the experience.
  I decided to try and port the flaskr app to Bottle
  Project: flaskr_to_bottler

  I started working on getting this all installed to my vm with a new virtualenv for Bottle. I was able to test the functionality by adding a simple Hello_World to confirm that it was working. I then copied the flaskr project over and began picking apart the differences. 

Templates:
I attempted to use jinja2_template from bottle in order to utilize the existing templates. Unfortunately, no matter where I place my *.html (views, templates), I get a 404 stating "Not found: '/'"
I did try to use the TEMPLATE_PATH.append("./templates") to force my app to use that directory but no dice.
Used the FlashPlugin: Imported bottle_flash
Used the SQLitePlugin: This allow for a call to be made to the db any time a route requires it. Handy instead of using 'g' 

Resources:
You must the resources.add_path() method to define where files like schema.sql will live. This was a gotchya when I tried to reinitialize a new bottler.db. After doing this, I still found that my entries table was not created, I had have to perform this manually by using the sqlite3 command to open a connection to bottler.db and create the table.

* Commit your changes to your fork of the class repository and send me a pull
  request





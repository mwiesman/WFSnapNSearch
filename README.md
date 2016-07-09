# WFSnapNSearch
Snap N' Search: An upholstered way to search (home goods including upholstery) (and find recommendations) using a quick snapshot photo.

+ Author: Mathew Wiesman
+ Author: Tianchu (Alex) Liang
+ Dates: 7/8/2016 - 7/10/2016

## About WFSnapNSearch

WFSnapNSearch was created as a project for the Wayfair hackathon. Our current project is built as a recommendation system for products based on your location. Using trained neural networks we will determine the location in which the photo was taken and then present a list of recommended items to the user as links to Wayfair.com. When dealing with recommendations we also determine some of the objects in the photo. These objects will compared with a recommendation list based off the determined location. The objects that are missing from the list are then presented as links to Wayfair.com.

--------------------
Setting Up
----------------------

```
1. Navigate to the main WFSnapNSearch directory
2. Make sure you have Caffe installed
3. run: pip install -r requirements.txt
	This should install all Modules necessary to run the project (if any are missing run pip install [module name] and please let us know)
```

-----------------------------------
Launching the WFSnapNSearch Web App
-------------------------------------
To run the WFSnapNSearch application:
```
1. Navigate to the main WFSnapNSearch directory 
2. run: python app.py
For getting recommendations on what itmes would go great in your location follow the 'b':
3b. Open your preferred browser and navigate to http://localhost:3006/wfsnapnsearch/recommender
4b. Upload your photo of the room you'd like recommendations for
5b. Bask in the glory of the products that will soon complement your room
For searching by photo (currently unavailable) follow the 'a':
3a. Open your preferred browser and navigate to http://localhost:3006/wfsnapnsearch/
4a. Upload your photo of the home good you wish to search
5a. Be amazed as the closest product to the product you always wanted is available for you to purchase 
```

----------------------------------
Future Vision
------------------------------------
The project goal was to train a neural network model on specifically Wayfair data to be used for image recognition and searching. The user could then provide an image of some product (whether it be a photo they had taken or one from online) to our project and the model would be able to determine as much about the image that would be relevant to find similar products on Wayfair.com. The information determined by the model would then be sent as a search query to Wayfair.com resulting in a "search by image" functionality.

----------
Notes
------------
This project does not reflect Wayfair.com and is seperate from the company
:shipit:
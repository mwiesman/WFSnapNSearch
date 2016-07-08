# WFSnapNSearch
Snap N' Search: An upholstered way to search (home goods including upholstery) using a quick snapshot photo.

+ Author: Mathew Wiesman
+ Author: Tianchu (Alex) Liang
+ Dates: 7/8/2016 - 7/10/2016

## About WFSnapNSearch

WFSnapNSearch was created as a project for the Wayfair hackathon. The project goal was to train a neural network model on specifically Wayfair data to be used for image recognition and searching. The user could then provide an image of some product (whether it be a photo they had taken or one from online) to our project and the model would be able to determine as much about the image that would be relevant to find similar products on Wayfair.com. The information determined by the model would then be sent as a search query to Wayfair.com resulting in a "search by image" functionality.

--------------------
Setting Up
----------------------

```
1. Navigate to the main WFSnapNSearch directory
2. run: pip install -r requirements.txt
	This should install all Modules necessary to run the project (if any are missing run pip install [module name] and please let us know)
```

-----------------------------------
Launching the WFSnapNSearch Web App
-------------------------------------
To run the WFSnapNSearch application:
```
1. Navigate to the main WFSnapNSearch directory 
2. run: python app.py
3. Open your preffered browser and navigate to http://localhost:3006/wfsnapnsearch/
4. Upload your photo of the home good you wish to search
5. Be amazed as the closest product to the product you always wanted is available for you to purchase
```

----------
Notes
------------
This project does not reflect Wayfair.com and is seperate from the company
:shipit:
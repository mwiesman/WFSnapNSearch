from flask import *
import os

recommender = Blueprint('recommender', __name__, template_folder='templates')

@recommender.route('/recommender', methods=['GET', 'POST'])
def rec_route():
	options = { 
        "recommend": False
	}

	return render_template("recommender.html", options=options)

@recommender.route('recommender/recommendations', methods=['GET', 'POST'])
def rec_rec_route():
	options = { 
        "recommend": True
	}

	validFormats = set(['png', 'jpg', 'bmp', 'gif'])
	baseUrl = "http://www.wayfair.com/keyword.php?keyword="
	if (request.form.get("op") == "img_search"):
	  	picFile = request.files.get("pic")
	  	if picFile:
	  		filename = picFile.filename
	  		extension = filename[-3:]
	  		# make sure the file is of a valid picture format
	  		if extension.lower() not in validFormats and filename[-4:].lower() not in ['tiff', 'jpeg']:
	  			abort(404)
	       	# save the uploaded image so we can send it to the model
	       	curPath = os.path.dirname(__file__)
	       	relPath = "static/images"
	       	imagesFolder = os.path.abspath(os.path.join(curPath, os.pardir, relPath))
	       	picFile.save(os.path.join(imagesFolder, filename))
	       	# Send the file to the trained model
	       	# loc = locationModel.recognize(filename)
	       	# imgObjects = objectModel.recognize(filename)
	       	# Look in dict[loc] for reccomended items
	       	# pull out overlap with imgObjects
	       	# store into recList a tuple (recommended item type (without location type), rec url)

	return render_template("recommender.html", options=options, loc=loc, recList=recList)
from flask import *
import os

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/', methods=['GET', 'POST'])
def main_route():
	validFormats = set(['png', 'jpg', 'bmp', 'gif'])
	print "here"
	print request.form.get("op")
	if (request.form.get("op") == "img_search"):
		print "here2"
	  	picFile = request.files.get("pic")
	  	print picFile
	  	if picFile:
	  		filename = picFile.filename
	  		print filename
	  		extension = filename[-3:]
	  		# make sure the file is of a valid picture format
	  		if extension.lower() not in validFormats and filename[-4:].lower() not in ['tiff', 'jpeg']:
	  			abort(404)
	       	# save the uploaded image so we can send it to the model
	       	curPath = os.path.dirname(__file__)
	       	relPath = "static/images"
	       	imagesFolder = os.path.abspath(os.path.join(curPath, os.pardir, relPath))
	       	picFile.save(os.path.join(imagesFolder, filename))
	       	print "pic saved"
	       	# Send the file to the trained model
	       	# model.recognize(filename)
	       	# returns JSON data to search by
	       	# store into set/list/just use the json object and grab the values for each key maybe
	       		#call container imageInfo
	       	#redirectURL = "http://www.wayfair.com/keyword.php?keyword="
	       	redirectURL = "http://www.wayfair.com/keyword.php?keyword=blue+lamp"
	       	# redirectURL += str(imageInfo[0]);
	       	# for attr in imageInfo[1:]:
	       	# 	redirectURL += ("+" + str(attr))
	       	print redirectURL
	       	return redirect(redirectURL)

	return render_template("index.html")
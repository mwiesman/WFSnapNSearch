from flask import *
import os

#from neural_network.blackbox import WF_Vision as WFV

recommender = Blueprint('recommender', __name__, template_folder='templates')

@recommender.route('/recommender', methods=['GET', 'POST'])
def rec_route():
	options = { 
        "recommend": False
	}

	return render_template("recommender.html", options=options)

@recommender.route('/recommender/recommendations', methods=['GET', 'POST'])
def rec_rec_route():
	options = { 
        "recommend": True
	}

	validFormats = set(['png', 'jpg', 'bmp', 'gif'])
	baseUrl = "http://www.wayfair.com/keyword.php?keyword="
	locationRecs = {
		"artstudio":["board", "toolbox", "easel", "pencil", "desk", "model", "brush", "bench", "smock", "paint"],
		"bar":["cabinet", "stool", "chair", "rack", "tap", "cart", "table", "mirror", "glassware", "opener", "jigger", "serveware"],
	 	"bathroom":["towel", "mat", "rug", "curtain", "sink", "faucet", "mirror", "shower", "tub", "toilet", "faucet", "bathrobe", "washcloth"],
	  	"bedroom":["bed", "headboard", "nightstand", "dresser", "armoire", "pillow", "bench", "comforter", "blanket", "sheet", "quilt", "lamp", "mirror", "rug", "clock", "curtain"],
	   	"children_room":["bed", "lamp", "rug", "light", "nightstand", "bookcase", "chair", "table", "bin", "toy", "tent"],
	    "classroom":["table", "desk", "chair", "board", "screen", "podium", "organizer", "bookcase", "cart", "stand", "cubby", "shelf"],
	    "dining_room":["table", "chair", "cabinet", "sideboard", "buffet", "stool", "bench", "chandelier", "cart", "art", "mirror", "candle", "tableware", "napkin", "vase", "coaster", "shaker", "ramekin", "cruet"],
	    "gameroom":["table", "chair", "pool", "arcade", "sign", "dart", "stool", "couch", "rug", "speaker"],
	    "garage":["rack", "shelf", "cabinet", "bin", "box", "workbench", "shed", "pegboard", "slatwall", "holder", "mat", "bag", "organizer"],
    	"kitchen":["cutlery", "board", "spatula", "strainer", "peeler", "grater", "bakeware", "toaster", "machine", "appliance", "blender", "cookware", "rack", "can", "sink", "light", "fan", "island"],
	    "livingroom":["chair", "table", "couch", "stand", "curtain", "rug", "pillow", "mirror", "ottoman", "lamp", "vase", "plant"],
	    "meeting_room":[], #redirect to office
	    "office":["table", "chair", "desk", "bookcase", "cabinet", "office", "mat", "lamp", "globe", "safe", "organizer"],
	    "restaurant":[]
	}
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
	       	picFile.save(os.path.join(imagesFolder, "target_image.jpg"))
	       	# Send the file to the trained model
	       	#WFModel = WFV("static/images")
	       	# List of possible locations recognized - first one has the highest accuracy
	       	#locList = WFModel.recognize_scene()
	       	locList = ["children_room", "bedroom", "gameroom"] #testing
	       	loc = locList[0]
	       	# objects recognized in the photo
	       	#imgObjects = WFModel.recognize_object()
	       	imgObjects = ["bed", "table"] #testing
	       	# Look in locationRecs[loc] for recommended items
	       	if loc == "children_room":
	       		locName = "kids"
	       	elif loc == "dining_room":
	       		locName = "dining room"
	       	elif loc == "livingroom":
	       		locName = "living room"
	       	elif loc == "meeting_room":
	       		loc = "office"
	       		locName = "office"
	       	elif loc == "restaurant":
	       		loc = "dining_room"
	       		locName = "dining room"
	       	else:
	       		locName = loc

	       	# store into recList a tuple (recommended item type (without location type), rec url)
	       	recList = []
	       	ownedObjs = []
	       	for rec in locationRecs[loc]:
	       		# don't include overlap with imgObjects
	       		if (rec not in imgObjects):
	       			recList.append((rec, baseUrl + locName + "+" + rec))
	       		else: #add them to items you already have
	       			ownedObjs.append(rec)
	       	return render_template("recommender.html", options=options, locName=locName, recList=recList, ownedObjs=ownedObjs, otherLocPos=locList[1:])
	       		



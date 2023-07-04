# import the modules
import os
import haversine as hs
from haversine import Unit
import requests
import urllib
import urllib.parse
import pandas as pd
import math

from PIL import Image
from PIL.ExifTags import TAGS


# class definition for image
class IMAGE:
    def __init__(self):
        self.filename = None
        self.initalMag = None
        self.height = None
        self.width = None
        self.ApertureValue = None
        self.MaxApertureValue = None
        self.BrightnessValue = None
        self.ExposureBiasValue = None
        self.FocalLength = None
        self.Make = None
        self.Model = None
        self.ExposureTime = None
        self.FNumber = None
        self.FOV = None
        self.FOVA = None  # field of view in arcminute
        self.pixelInDegree = None
        self.observeLoc = None  # observation point
        self.targetLoc = None  # target building

    def __str__(self):  # CHANGE THIS TO CHANGE THE AMOUNT OF INFO OUTPUT FOR EACH IMAGE
        return str(self.initalMag) + ',' + str(self.height) + ',' + str(self.width) + ',' + str(self.ApertureValue) + \
               ',' + str(self.MaxApertureValue) + ',' + str(self.BrightnessValue) + ',' + str(self.ExposureBiasValue) \
               + ',' + str(self.FocalLength) + ',' + str(self.Make) + ',' + str(self.Model) + ',' + \
               str(self.ExposureTime) + ',' + str(self.FNumber) + ',' + str(self.FOV) + ',' + str(
            self.FOVA) + ',' + str(self.pixelInDegree) + ',' + \
               str(self.observeLoc) + ',' + str(self.targetLoc)


# class definition for location
class LOCATION:
    def __init__(self):
        self.address = None
        self.latitude = 0
        self.longitude = 0
        self.altitude = 0
        self.height = 0
        self.heightA = 0  # height in arcminute
        self.width = 0
        self.widthA = 0  # width in arcminute

    def __str__(self):
        return str(round(self.latitude, 3)) + ',' + str(round(self.longitude, 3)) + ',' + str(
            round(self.altitude, 3)) + ',' + \
               str(round(self.height, 3)) + ',' + str(round(self.heightA, 3)) + ',' + str(
            round(self.width, 3)) + ',' + str(round(self.widthA, 3))


# USGS Elevation Point Query Service
urlElev = r'https://epqs.nationalmap.gov/v1/json?'

# folder_dir
folder_dir = "D:/Stanford/Hyperacuity/Hyperacuity"

# locations
observe_loc = LOCATION()
target_loc = LOCATION()

# Horizontal frame size : https://www.digicamdb.com/specs/canon_eos-rebel-t3i/ (in mm)
frame_size = 22.3


############################################################


def create_images_dict(images):
    # get the path/directory

    # create image dictionary
    for imagename in os.listdir(folder_dir):

        # check if the image ends with png
        if imagename.endswith(".JPG"):
            image = Image.open(imagename)

            # create IMAGE instance
            instance = IMAGE()

            # extract other basic metadata
            info_dict = {
                "Filename": image.filename,
                "Image Height": image.height,
                "Image Width": image.width,
                "Image Format": image.format,
                "Image Mode": image.mode,
                "Image is Animated": getattr(image, "is_animated", False),
                "Frames in Image": getattr(image, "n_frames", 1)
            }

            # store to instance class
            instance.filename = image.filename
            if 'Max' in image.filename:
                instance.initalMag = 300
            else:
                instance.initalMag = 75
            instance.height = image.height
            instance.width = image.width

            exifdata = image.getexif()

            for tag_id in exifdata:
                # get the tag name, instead of human unreadable tag id
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                # decode bytes
                if isinstance(data, bytes) and tag != "MakerNote":
                    data = data.decode()
                if tag == "ApertureValue":
                    instance.ApertureValue = data
                if tag == "MaxApertureValue":
                    instance.MaxApertureValue = data
                if tag == "BrightnessValue":
                    instance.BrightnessValue = data
                if tag == "ExposureBiasValue":
                    instance.ExposureBiasValue = data
                if tag == "FocalLength":
                    instance.FocalLength = data
                if tag == "Make":
                    instance.Make = data
                if tag == "Model":
                    instance.Model = data
                if tag == "ExposureTime":
                    instance.ExposureTime = data
                if tag == "FNumber":
                    instance.FNumber = data

            # provide infomation about the observation point and target building
            instance.observeLoc = observe_loc.__str__()
            instance.targetLoc = target_loc.__str__()

            # store instance to dictionary
            images[instance.filename] = instance


def elevation_function(df, lat_column, lon_column):
    """Query service using lat, lon. add the elevation values as a new column."""
    elevations = []
    for lat, lon in zip(df[lat_column], df[lon_column]):
        # define rest query params
        params = {
            'x': lon,
            'y': lat,
            "wkid": 4326,
            'units': 'Feet',
            'includeDate': 'false'
        }

        # format query string and return query value
        result = requests.get((urlElev + urllib.parse.urlencode(params)))
        elevations.append(result.json()['value'])

    df['elev_feet'] = elevations


def gather_location_info():
    global info
    with open('observation location.txt') as oloc:
        next(oloc)
        for line in oloc:
            line = line.strip()
            loc = line.split(',')
            observe_loc.latitude = float(loc[0])
            observe_loc.longitude = float(loc[1])
    with open('target location - 181 fremont.txt') as tloc:
        next(tloc)
        info = tloc.readlines()
        target_loc.address = info[0].strip()
        target_loc.height = float(info[1].strip())
        target_loc.width = float(info[2].strip())


def compute_relevant_location():
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(target_loc.address) + '?format=json'
    response = requests.get(url).json()
    target_loc.latitude = float(response[0]["lat"])
    target_loc.longitude = float(response[0]["lon"])
    # calculate altitude
    lat = [observe_loc.latitude, target_loc.latitude]
    lon = [observe_loc.longitude, target_loc.longitude]
    # create data frame
    df = pd.DataFrame({
        'lat': lat,
        'lon': lon
    })
    elevation_function(df, 'lat', 'lon')
    df.head()
    alt = df['elev_feet']
    observe_loc.altitude = float(alt[0])
    target_loc.altitude = float(alt[1])


def compute_building_property():
    # target building property
    target_loc.height = float(target_loc.height) + target_loc.altitude - float(observe_loc.altitude)
    target_loc.heightA = math.degrees(math.atan(target_loc.height / aerial_distance)) * 60
    target_loc.width = float(target_loc.width)
    target_loc.widthA = math.degrees(math.atan(target_loc.width / aerial_distance)) * 60


def compute_FOV():
    for image in images:
        focalLength = images[image].FocalLength
        images[image].FOV = math.degrees(2 * math.atan(frame_size / (focalLength * 2)))
        images[image].FOVA = images[image].FOV * 60
        images[image].pixelInDegree = (1 / images[image].width) * images[image].FOVA


########################################################

# initialize images structure
images = {}

# read in location info from "observation location.txt" and "target location.txt"
gather_location_info()

# compute information regarding observation and target location
compute_relevant_location()

# compute aerial distance
aerial_distance = hs.haversine((observe_loc.latitude, observe_loc.longitude),
                               (target_loc.latitude, target_loc.longitude), unit=Unit.FEET)

# compute height and width of target building in visual degrees
compute_building_property()

# create a dictionary of meta-data of images in the current folder
create_images_dict(images)

# update field of view
compute_FOV()

# output txt file
with open('result_181_fremont.csv', 'w') as file:
    file.write(
        "Participants #,inital magnification(mm),height,width,aperture,max aperture,brightness,exposure bias,focal length,make,model,exposure time,fnumber,field of view,field of view(arcminute),arcminute degree in each pixel,observation point(latitude),observation point(longitude),observation point(altitude),observation point(relative height(feet)),observation point(relative height(arcminute)),observation point(width(feet)),observation point(width(arcminute)),target location(latitude),target location(longitude),target location(altitude),target location(relative height(feet)),target location(relative height(arcminute),target location(width(feet)),target location(width(arcminute))\n")
    for filename in images:
        instance = images[filename]
        info = instance.__str__()
        file.write(filename.split('-')[0].strip() + "," + info + '\n')

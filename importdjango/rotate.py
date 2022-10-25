import os 
import sys
import subprocess
import time
import tablib
from import_export import resources

from web_app.resources import TopicResource, \
    EventResource, HomeImageResource, DonateTopicResource, \
    DonatePostResource, BlogTopicResource, BlogPostResource, \
    ImageGalleryResource, SermonsResource, Main_page_aboutResource, \
    Main_page_eventsResource

# list the files in generatedcsv folder
os.system('ls -l generatedcsv')
# generate random name for the csv file
import random
import string
#random project name
project_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
print("project_name: ", project_name)
# tar cfzv generated csv folder to backupcsv with name project_name
os.system('tar cfzv backupcsv/' + project_name + '.tar.gz generatedcsv') 

# create tablib dataset from generatedcsv folder

# add event_data.csv to dataset
with open('generatedcsv/event_data.csv', 'r') as f:
    # create tablib dataset from csv file
    dataset = tablib.Dataset().load(f.read())
    # dataset remove headers

   # import the dataset to the database
    EventResource().import_data(dataset, dry_run=False)
    f.close()

# add blogpost_data.csv to dataset
with open('generatedcsv/blogpost_data.csv', 'r') as f:
    # create tablib dataset from csv file
    dataset = tablib.Dataset().load(f.read())
    # dataset remove headers

   # import the dataset to the database
    BlogPostResource().import_data(dataset, dry_run=False)
    f.close()

# add homeimage_data.csv to dataset
with open('generatedcsv/homeimage_data.csv', 'r') as f:
    # create tablib dataset from csv file
    dataset = tablib.Dataset().load(f.read())
    # dataset remove headers

   # import the dataset to the database
    HomeImageResource().import_data(dataset, dry_run=False)
    f.close()

# add imagegallery_data.csv to dataset
with open('generatedcsv/imagegallery_data.csv', 'r') as f:
    # create tablib dataset from csv file
    dataset = tablib.Dataset().load(f.read())
    # dataset remove headers

   # import the dataset to the database
    ImageGalleryResource().import_data(dataset, dry_run=False)
    f.close()
# add mainpageabout_data.csv to dataset
with open('generatedcsv/mainpageabout_data.csv', 'r') as f:
    # create tablib dataset from csv file
    dataset = tablib.Dataset().load(f.read())
    # dataset remove headers

   # import the dataset to the database
    Main_page_aboutResource().import_data(dataset, dry_run=False)
    f.close()



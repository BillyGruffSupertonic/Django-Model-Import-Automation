import time
import os 
import tablib
from import_export import resources
from web_app.models import Events, HomeImage, \
     Topic, DonateTopic, DonatePost, BlogTopic, \
          BlogPost, ImageGallery, Sermons, \
              Main_page_about, Main_page_events,\
                   Comment, BibleVerse, Ministry


current_time = time.strftime("%Y-%m-%d")
year = current_time.split('-')[0]
month = current_time.split('-')[1]
day = current_time.split('-')[2]

# make sure there is a ~/backupcsv folder
if not os.path.exists('backupcsv'):
    os.makedirs('backupcsv')
else:
    print("backupcsv folder exists")

# make sure there is a ~/generatedcsv folder
if not os.path.exists('generatedcsv'):
    os.makedirs('generatedcsv')
else:
    print("generatedcsv folder exists")

# generate a random name for the csv file
import random
import string
#random project name 
project_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
print("project_name: ", project_name)

images_folder = '/mnt/chromeos/GoogleDrive/MyDrive/cocb/'

# check if media folder has a folder named imported_csv
if not os.path.exists('media/imported_csv'):
    # make directory 
    os.makedirs('media/imported_csv')
    # make directory current time year-month-day
    # get the year, month, day
    
    
    
else:
    print("media/imported_csv folder exists")
    # remove all in the folder
    os.system('rm -rf media/imported_csv/*')


os.makedirs('media/imported_csv/' + year + '-' + month + '-' + day)


# remove all items 

# walk find all files in images_folder
for root, dirs, files in os.walk(images_folder):
    # move all files to media/imported_csv
    for file in files:
        # get path of file to be moved
        path = os.path.join(root, file)
        # get path of destination folder
        destination = os.path.join('media/imported_csv', year + '-' + month + '-' + day)
        # copy the file to destination
        os.system('cp ' + path + ' ' + destination)
print("files moved to media/imported_csv")

# delete files in generatedcsv folder
for root, dirs, files in os.walk('generatedcsv'):
    for file in files:
        path = os.path.join(root, file)
        os.remove(path)
# print all csv files in web_app/tables
for root, dirs, files in os.walk('web_app/tables'):
    for file in files:
        # if file is a csv file
        if file.endswith('.csv'):
        # open the file

            with open(os.path.join('web_app/tables', file), 'r') as f:
                # load the csv file
                data = tablib.Dataset().load(f.read())
                
                f.close()
        # 
        # print new_data
        print('type(data): ', type(data))
       

        # if image is in the csv in data
        if 'image' in data.headers:
            # write data.headers to generatedcsv file 
            print("data.headers: ", data.headers)

            # write data to generatedcsv file
            with open(os.path.join('generatedcsv', file), 'w') as f:
                for header in data.headers:
                    f.write(header + ',')
                f.write('\n')
                # get rows 
                rows = data.dict
                # get image column
              
                for row in rows:
                    # get a random image from media/imported_csv
                    randimage = random.choice(os.listdir('media/imported_csv' + '/' + year + '-' + month + '-' + day))
                  
                    # replaec image with random image in media/imported_csv folder
                    row['image'] = 'imported_csv/' + year + '-' + month + '-' + day + '/' + randimage
                    # change rowid
                 
                    # write append entire row to generatedcsv file
                    # print(row)
                    print("row: ", row)
                    # write row to generatedcsv file
                    for segment in row:
                        f.write(row[str(segment)] + ',')
                    f.write('\n')
                      

            f.close()
                    
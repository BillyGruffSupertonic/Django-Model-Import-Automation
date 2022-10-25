from web_app.resources import TopicResource, \
    EventResource, HomeImageResource, DonateTopicResource, \
    DonatePostResource, BlogTopicResource, BlogPostResource, \
    ImageGalleryResource, SermonsResource, Main_page_aboutResource, \
    Main_page_eventsResource

import os 
# delete items in web_app/tables if they exist
for root, dirs, files in os.walk('web_app/tables'):
    # if item is a csv file
    for file in files:
        if file.endswith('.csv'):
            # delete the file
            os.remove(os.path.join('web_app/tables', file))

event_data = EventResource().export()
print("Event Data ---------")
print(event_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'event_data.csv'), 'w') as f:
    f.write(event_data.csv)

    f.close()

topic_data = TopicResource().export()
print("Topic Data ---------")
print(topic_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'topic_data.csv'), 'w') as f:
    f.write(topic_data.csv)

    f.close()

HomeImage_data = HomeImageResource().export()
print("HomeImage Data ---------")
print(HomeImage_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'homeimage_data.csv'), 'w') as f:
    f.write(HomeImage_data.csv)

    f.close()

DonateTopicResource_data = DonateTopicResource().export()
print("DonateTopic Data ---------")
print(DonateTopicResource_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'donatetopic_data.csv'), 'w') as f:
    f.write(DonateTopicResource_data.csv)

    f.close()



DonatePostResource_data = DonatePostResource().export()
print("DonatePost Data ---------")
print(DonatePostResource_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'donatepost_data.csv'), 'w') as f:
    f.write(DonatePostResource_data.csv)

    f.close()

BlogTopic_data = BlogTopicResource().export()
print("BlogTopic Data ---------")
print(BlogTopic_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'blogtopic_data.csv'), 'w') as f:
    f.write(BlogTopic_data.csv)

    f.close()

BlogPost_data = BlogPostResource().export()
print("BlogPost Data ---------")
print(BlogPost_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'blogpost_data.csv'), 'w') as f:
    f.write(BlogPost_data.csv)

    f.close()

ImageGallery_data = ImageGalleryResource().export()
print("ImageGallery Data ---------")
print(ImageGallery_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'imagegallery_data.csv'), 'w') as f:
    f.write(ImageGallery_data.csv)

    f.close()

Sermon_data = SermonsResource().export()
print("Sermon Data ---------")
print(Sermon_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'sermons_data.csv'), 'w') as f:
    f.write(Sermon_data.csv)

    f.close()

mainpageabout_data = Main_page_aboutResource().export()
print("Main_page_about Data ---------")
print(mainpageabout_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'mainpageabout_data.csv'), 'w') as f:
    f.write(mainpageabout_data.csv)

    f.close()

mainpageevents_data = Main_page_eventsResource().export()
print("Main_page_events Data ---------")
print(mainpageevents_data.csv)
# safe to csv file in web_app tables folder
with open(os.path.join('web_app', 'tables', 'mainpageevents_data.csv'), 'w') as f:
    f.write(mainpageevents_data.csv)

    f.close()









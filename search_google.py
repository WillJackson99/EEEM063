
from google_images_download import google_images_download

#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"Ferrari 312T, Mclaren mp4/4, Mercedes w10, Ferrari F2004, Williams FW18",
             "limit":200,"print_urls":False, 
             "chromedriver":"/home/will/Downloads/chromedriver",
             "format":"jpg",
             "color_type":"full-color",
             "type":"photo",}

paths = response.download(arguments)

#print complete paths to the downloaded images
print(paths)


###############Similar images
#f2004 = 
#sf1000 =
#641 =
#312T =
#156 =


#####################################
#Bing
'''
from bing_image_downloader import downloader
downloader.download("monkey", limit=200,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("tiger", limit=200,  output_dir='dataset', 
                    adult_filter_off=True, force_replace=False, timeout=60)

                    '''
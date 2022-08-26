import base64
import os
import random
import urllib.request
import zipfile

do_not_track = false
download_url = 'https://www.dcaiti.tu-berlin.de/research/simulation/downloads/get/best-scenario-v1.zip'

if os.path.exists('berlin.sumocfg'):
    print('BeST scenario already exists, skipping')
else:
    print('Downloading BeST scenario ...')
    if do_not_track:
        urllib.request.urlretrieve(download_url, 'best-scenario.zip')
    else:
        urllib.request.urlretrieve(download_url + '&record=true', 'best-scenario.zip')
    print('Unzipping ...')
    with zipfile.ZipFile('best-scenario.zip', 'r') as best_zip:
        best_zip.extractall()
    os.remove('best-scenario.zip')
    print('Finished')
    



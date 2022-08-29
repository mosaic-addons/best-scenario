import os
import urllib.request
import zipfile

# Set to True if no tracking record (anonymized) should be generated on www.dcaiti.tu-berlin.de.
do_not_track = True 

download_url = 'https://www.dcaiti.tu-berlin.de/research/simulation/downloads/get/best-scenario-v1.zip'

if os.path.exists('berlin.sumocfg'):
    print('BeST scenario already exists, skipping')
else:
    def report_progress(block_n, block_size, complete_size):  
        progress = 100.0 * min(1.0, block_n * block_size / complete_size)
        print('Downloading BeST scenario ... {}%'.format(int(progress)), end='\r');

    print('Downloading BeST scenario ...', end='\r')
    if do_not_track:
        urllib.request.urlretrieve(download_url, filename='best-scenario.zip', reporthook=report_progress)
    else:
        urllib.request.urlretrieve(download_url + '?record=true', filename='best-scenario.zip', reporthook=report_progress)
    print('Unzipping ...')
    with zipfile.ZipFile('best-scenario.zip', 'r') as best_zip:
        best_zip.extractall()
    os.remove('best-scenario.zip')
    print('Finished')
    



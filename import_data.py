import requests, io, gzip, tarfile, os, shutil, pandas as pd
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

movie_url = 'http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz'
imdb_title_url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
imdb_rating_url = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
bo_mojo_url = 'https://www.boxofficemojo.com'
kaggle_awards_name = 'unanimad/the-oscar-award'

data_target = './data'
movie_target    = data_target + '/MovieSummaries'
imdb_target     = data_target + '/imdb'
bo_mojo_target  = data_target + '/bo_mojo'
kaggle_target   = data_target + '/kaggle'

def check_target(to):
    if os.path.exists(to):
        # ask user if they want to overwrite
        print("\033[91mDirectory {} already exists".format(to))
        response = input("Do you want to overwrite? (y/n): \033[0m")
        if response.lower() == 'y':
            print("Overwriting existing directory")
            shutil.rmtree(to)
            os.mkdir(to)
            return True
        else:
            return False
    return True

# add function "download_data" that download a dataset from a given URL
def download_movie_data(url, to):
    print("Downloading data from {}".format(url))
    r = requests.get(url, stream=True)
    if r.ok:
        print("Decompressing data to {}".format(to))
        tar = tarfile.open(fileobj=gzip.GzipFile(fileobj=io.BytesIO(r.content)))
        tar.extractall(path=to)
        print("Download complete\n")

def download_imdb_data(url, to):
    if not os.path.exists(imdb_target):
        os.mkdir(imdb_target)        

    print("Downloading data from {}".format(url))
    r = requests.get(url, stream=True)
    if r.ok:
        print("Decompressing data to {}".format(to))
        gzip_obj = gzip.GzipFile(fileobj=io.BytesIO(r.content))
        with open(to, 'xb') as f:
            shutil.copyfileobj(gzip_obj, f)
        print("Download complete\n")

def download_box_office_mojo(url, to):
    if not os.path.exists(bo_mojo_target):
        os.mkdir(bo_mojo_target)

    print("Downloading data from {}".format(url))
    BODS = {'Title': [], 'Year': [], 'Worldwide': [], 'Domestic': [], 
            'Domestic_percent': [], 'Foreign': [], 'Foreign_percent': []}
    r = requests.get(url+'/year/world/?ref_=bo_nb_cso_tab')
    if r.ok:
        years = bs(r.text, 'html.parser').find_all('option')
        for year in tqdm(years):
            r = requests.get(bo_mojo_url + year['value'])
            if r.ok:
                soup = bs(r.text, 'html.parser')
                rows = soup.find_all('tr')[1:]
                for row in rows:
                    cols = row.find_all('td')
                    BODS['Title'].append(cols[1].text)
                    BODS['Year'].append(year.text)
                    BODS['Worldwide'].append(cols[2].text)
                    BODS['Domestic'].append(cols[3].text)
                    BODS['Domestic_percent'].append(cols[4].text)
                    BODS['Foreign'].append(cols[5].text)
                    BODS['Foreign_percent'].append(cols[6].text)
        box_office = pd.DataFrame(BODS)
        box_office.to_csv(to, index = None)
        print("Download complete\n") 

def download_awards(name, to):
    os.environ['KAGGLE_KEY'] = 'bacc9cd361a5492f423e26574f5de1af'
    os.environ['KAGGLE_USERNAME'] = 'thohoule'
    import kaggle
    
    worked = False
    while not worked:
        try:
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(name, path=to, unzip=True, quiet=False)
            worked = True
        except:
            print("\033[91mDefault autentication tokens didn't work, please go to kaggle, connect and create a token \033[0m\n")
            username = str(input("username: "))
            key = str(input("key: "))
            os.environ['KAGGLE_KEY'] = key
            os.environ['KAGGLE_USERNAME'] = username
            worked = False

def main():
    

    check_target(data_target)
    # Download movies data        
    if check_target(movie_target):
        download_movie_data(movie_url, data_target)

    # Download IMDB data
    if check_target(imdb_target):
        download_imdb_data(imdb_names_url, imdb_target+'/imdb_names.tsv')
        download_imdb_data(imdb_principals_url, imdb_target+'/imdb_principals.tsv')
        download_imdb_data(imdb_title_url, imdb_target+'/imdb_titles.tsv')
        download_imdb_data(imdb_rating_url, imdb_target+'/imdb_ratings.tsv')

    # Download box office mojo data
    if check_target(bo_mojo_target):
        download_box_office_mojo(bo_mojo_url, bo_mojo_target+'/bo_mojo.csv')

    # Download awards dataset
    if check_target(kaggle_target):
        download_awards(kaggle_awards_name, kaggle_target)
        

if __name__ == "__main__":
    main()

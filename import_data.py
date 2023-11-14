import requests, io, gzip, tarfile, os, shutil, pandas as pd
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

movie_url = 'http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz'
imdb_names_url = 'https://datasets.imdbws.com/name.basics.tsv.gz'
imdb_principals_url = 'https://datasets.imdbws.com/title.principals.tsv.gz'
imdb_title_url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
imdb_rating_url = 'https://datasets.imdbws.com/title.ratings.tsv.gz'
bo_mojo_url = 'https://www.boxofficemojo.com'

data_target = './data'
movie_target = './data/MovieSummaries'
imdb_target = './data/imdb'
bo_mojo_target = './data/bo_mojo'

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

def check_target(to):
    if os.path.exists(to):
        # ask user if they want to overwrite
        print("Data directory already exists")
        response = input("Do you want to overwrite? (y/n): ")
        if response.lower() == 'y':
            print("Overwriting existing directory")
            shutil.rmtree(to)
            os.mkdir(to)
            return True
        else:
            print("Exiting")
            return False
    return True

def main():
    if check_target(data_target):
        # Download movies data        
        download_movie_data(movie_url, data_target)

        # Download IMDB data
        download_imdb_data(imdb_names_url, imdb_target+'/imdb_names.tsv')
        download_imdb_data(imdb_principals_url, imdb_target+'/imdb_principals.tsv')
        download_imdb_data(imdb_title_url, imdb_target+'/imdb_titles.tsv')
        download_imdb_data(imdb_rating_url, imdb_target+'/imdb_ratings.tsv')
        
        # Download box office mojo data
        download_box_office_mojo(bo_mojo_url, bo_mojo_target+'/bo_mojo.csv')
        

if __name__ == "__main__":
    main()

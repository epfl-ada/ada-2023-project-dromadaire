import requests, io, gzip, tarfile, os, shutil

movie_url = 'http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz'
imdb_title_url = 'https://datasets.imdbws.com/title.basics.tsv.gz'
imdb_rating_url = 'https://datasets.imdbws.com/title.ratings.tsv.gz' 

data_target = './data'
movie_target = './data/MovieSummaries'
imdb_target = './data/imdb'

# add function "download_data" that download a dataset from a given URL
def download_movie_data(url, to):
    print("Downloading data from {}".format(url))
    r = requests.get(url, stream=True)
    if r.ok:
        print("Decompressing data to {}".format(to))
        tar = tarfile.open(fileobj=gzip.GzipFile(fileobj=io.BytesIO(r.content)))
        tar.extractall(path=to)
        print("Download complete")

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
        print("Download complete")

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
        download_imdb_data(imdb_title_url, imdb_target+'/imdb_titles.tsv')
        download_imdb_data(imdb_rating_url, imdb_target+'/imdb_ratings.tsv')
        

if __name__ == "__main__":
    main()
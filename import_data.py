import requests, io, gzip, tarfile, os, shutil

data_url = 'http://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz'
data_target = './data'

# add function "download_data" that download a dataset from a given URL
def download_data(url, to):
    print("Downloading data from {}".format(url))
    r = requests.get(url, stream=True)
    if r.ok:
        print("Decompressing data to {}".format(to))
        tar = tarfile.open(fileobj=gzip.GzipFile(fileobj=io.BytesIO(r.content)))
        tar.extractall(path=to)
        print("Download complete")

def check_target(to):
    if os.path.exists(to):
        # ask user if they want to overwrite
        print("Target directory already exists")
        response = input("Do you want to overwrite? (y/n): ")
        if response.lower() == 'y':
            print("Overwriting existing directory")
            shutil.rmtree(to)
            os.mkdir(to)
            return True
        else:
            print("Exiting")
            return False

def main():
    if check_target(data_target):
        download_data(data_url, data_target)
        

if __name__ == "__main__":
    main()
        
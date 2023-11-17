# Import data

In order to run the jupyter notebooks, you will need to download the dataset. To get it you can simply run the `import_data.py` script. If that doesn't work you can do it manually.

### Manually
1. Go to http://www.cs.cmu.edu/~ark/personas/ and in "Download" click on the the hyper link "dataset" to download the dataset
2. Unzip the files into a new folder `./data` at the same level as this README.
3. Then go to https://datasets.imdbws.com/ and download `title.basics.tsv.gz` and `title.ratings.tsv.gz` 
4. Decompress the two files in a new folder `./data/imdb/`


### Using the script

Run

```bash
pip install -r requirements.txt
python3 import_data.py
```

Your data folder should look like this:

```
data/
└── MovieSummaries/    
    ├── character.metadata.tsv 
    ├── movie.metadata.tsv
    ├── name.clusters.txt
    ├── plot_summaries.txt
    ├── README.txt
    └── tvtropes.clusters.txt
└── imdb/  
    ├── imdb_titles.tsv
    └── imdb_ratings.tsv
└── bo_mojo/  
    └── bo_mojo.csv

```

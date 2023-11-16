# Import data

In order to run the jupyter notebooks, you will need to download the dataset. To get it you can simply run the `import_data.py` script. If that doesn't work you can do it manually.

### Manually
1. Go to http://www.cs.cmu.edu/~ark/personas/ and in "Download" click on the the hyper link "dataset" to download the dataset
2. Unzip the files into a new folder `./data` at the same level as this README.
3. Then go to https://datasets.imdbws.com/ and download `title.basics.tsv.gz` and `title.ratings.tsv.gz` 
4. Decompress the two files in a new folder `./data/imdb/`
5. Go to https://www.kaggle.com/datasets/unanimad/the-oscar-award/data and download the dataset (login is required). Then unzip the file in `./data/kaggle/`


### Using the script

Run

```bash
pip install -r requirements.txt
python3 import_data.py
```

:warning: The script will download the kaggle dataset using their API so you need to have it installed (`pip install kaggle`, or use the requirements) and it will use token to authenticate. If the autentication doesn't work, you need to go to kaggle, connect to your account (or create one) and then in the account parameter in the section "API", select "create token". This will generate a `kaggle.json` file. Copy and paste the username and key from this file when requested in the command line.

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
└── kaggle/  
    └── the_oscar_award.csv

```
# Import data

In order to run the jupyter notebooks, you will need to download the dataset. To get it you can simply run the `import_data.py` script. If that doesn't work you can do it manually.

### Manually
1. Go to http://www.cs.cmu.edu/~ark/personas/ and in "Download" click on the the hyper link "dataset" to download the dataset
2. Unzip the files into a new folder `./data` at the same level as this README.


### Using the script

Run

```bash
python3 import_data.py
```

You need the `requests` python module to use the script. You can install it using (you will have it by default if used installed all the requirements from the `requirements.txt` file):

```bash
pip install requests
``` 

Your data folder should look like this:

```
data/
└── MovieSummaries/    
    ├── character.metadata.csv 
    ├── movie.metadata.csv
    ├── name.clusters.txt
    ├── plot_summaries.txt
    ├── README.txt
    └── tvtropes.clusters.txt
```

## Rendu P2

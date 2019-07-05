# RW-LMLM
The code of the paper *Capturing Semantic and Syntactic Information for Link Prediction in Knowledge Graphs* (In ISWC2019)
## Requirements
* python 3.7
* pytorch 1.0.1
* torchtext 0.3.1
* numpy 1.16.2
* cuda >= 9.0

## Project structure
* **data** // data for training and evaluation
	* **raw**	// raw data
	* **id**	// numerical version of raw data, reducing storage space
	* **graph** // graphs generated by all triples; used for filt. setting
	* **rw**	// training data generated by random walks on training set as well as testing set and validation set in the form &lt; h, t, r &gt; or &lt; t, h, -r &gt;

* **preprocess**	// code for data preprocessing, including creating data iterator, creating graph, and random walks

* **model**		// code of LMLM, also includes the implementation of transformer decoder
* **train**		// code for training and evaluation

## Run
We give a complete running example on WN18RR.
Please note that we have provided some training data generated by random walks, which are compressed (e.g. *data/rw/wn18rr_id/train_50_10.zip*). You can use them after uncompressing or generate the data by following step 1. The results of different training  data may be slightly different. We also provide some model parameters of WN18RR (*example/wn18rr/parameters/*), which can be used directly for evaluation.
* `python rw_wn18rr.py`	
Perform random walks on the graph converted by training set. This will generate a csv file in *data/rw/wn18rr_id/* for training. 

* `python train_wn18rr.py`
Train LMLM with the data generated in the previous step. You can specify the file paths in the code to save model parameters and log file. 

* `python test_wn18rr.py`
Evaluate on validation set and testing set. You need to specify the folder where the model parameter files are located in the code.

## References
* datasets:
[WN18](https://everest.hds.utc.fr/doku.php?id=en:transe), [FB15k](https://everest.hds.utc.fr/doku.php?id=en:transe), [WN18RR](https://github.com/TimDettmers/ConvE), [FB15k-237](https://www.microsoft.com/en-us/download/details.aspx?id=52312)
* The implementation of Transformer refers to [this](http://nlp.seas.harvard.edu/2018/04/03/attention.html) and [this](https://github.com/jadore801120/attention-is-all-you-need-pytorch).
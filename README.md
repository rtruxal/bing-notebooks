 Bing Search API High-Level Docs (Unofficial)
==================================
# Bing's API Endpoints:

 - General Web: https://api.cognitive.microsoft.com/bing/v7.0/search?
 - News: 
 - Image: https://api.cognitive.microsoft.com/bing/v7.0/images/search?
   - Image Details: https://api.cognitive.microsoft.com/bing/v7.0/images/details?
   - Trending Images: https://api.cognitive.microsoft.com/bing/v7.0/images/trending
 - Video: 
 - Entity:
 - Spellcheck:
 - Autocorrect:
 - Custom:  


### Important blurbs

In the following two URLs I'm searching the internet for kitten pictures.

  A) `https://api.cognitive.microsoft.com/bing/v7.0/search?q=kittens&responseFilter=Images`   
  
  B) `https://api.cognitive.microsoft.com/bing/v7.0/images/search?q=kittens`


In A), I'm searching the web endpoint 

# Prerequisites
 - Python 3 (Written using python3.7)
   - w/ the `jupyter-notebook`, &  `requests` packages installed
 - A Bing Search API V7 Trial Tier.
   - For Web, News, Image, Video, or Entity search, you will need a free-tier (F0) "Bing Search v7" subscription. [!websearch-free-tier](local/websearch-free-tier.PNG)
   - For Spellcheck, Autocorrect, or Custom Search, you will need free-tier (F0) "Bing Spell Check v7," "Bing Autosuggest v7," & "Bing Custom Search" subscriptions respectively.   
[!other-free-tiers](https://raw.githubusercontent.com/rtruxal/github-pics/master/bingdoc%20images/spell-auto-and-custom-free-tiers.png)
### Getting python & jupyter:
You must have python installed, and your current environment should be python 3.X. Try typing `python --version` into your shell of choice.

If you do not see `python3.<something>` after running this command, you need to either install python, create a virtual environment, or both.  
If you are new to python, I suggest using the 3.7 version of [Anaconda](https://www.anaconda.com/distribution/#download-section). MAKE SURE TO SLECT THE CORRECT OPERATING SYSTEM AT THE TOP OF THAT PAGE.   

Here is a link to their [installation instructions](https://docs.anaconda.com/anaconda/install/).  

Once you have installed anaconda and added the correct files to your `$PATH|%PATH%`, use the command `conda install jupyter-notebook requests` to fulfil the final prerequisites.

### Getting a Bing Search API Subscription:

\<PLACEHOLDER>


# Setup:

### Windows:
```cmd
> git clone https://github.com/rtruxal/bing-api-guide.git
> cd bing-api-guide
> set BING_KEY=1234567890deadbeef0987654321
> jupyter notebook
```
### Linux/Mac
```sh
$ git clone https://github.com/rtruxal/bing-api-guide.git
$ cd bing-api-guide
$ export BING_KEY=1234567890deadbeef0987654321
$ jupyter notebook
```





 Bing Search API Jupyter Notebooks
==================================

# Prerequisites
 - Python 3 (Written using python3.7)
   - w/ the `jupyter-notebook`, &  `requests` packages installed
 - A Bing Search API V7 Trial Tier.
   - For Web, News, Image, Video, or Entity search, you will need a free-tier (F0) "Bing Search v7" subscription. [!websearch-free-tier](img/websearch-free-tier.PNG)
   - For Spellcheck, Autocorrect, or Custom Search, you will need free-tier (F0) "Bing Spell Check v7," "Bing Autosuggest v7," & "Bing Custom Search" subscriptions respectively.   
[!other-free-tiers](https://raw.githubusercontent.com/rtruxal/github-pics/master/bingdoc%20images/spell-auto-and-custom-free-tiers.png)


# Setup:

### On Windows:
```cmd
> git clone https://github.com/rtruxal/bing-api-guide.git
> cd bing-api-guide
> set BING_KEY=1234567890deadbeef0987654321
> jupyter notebook
```
### On Linux/Mac
```sh
$ git clone https://github.com/rtruxal/bing-api-guide.git
$ cd bing-api-guide
$ export BING_KEY=1234567890deadbeef0987654321
$ jupyter notebook
```



# Other/Misc  


### Are You Using the Right Endpoint?

The following two URLs both work, but have **very different behavior**. In both, I'm searching the internet for kitten pictures.

  A) `https://api.cognitive.microsoft.com/bing/v7.0/search?q=kittens&responseFilter=Images`   
  
  B) `https://api.cognitive.microsoft.com/bing/v7.0/images/search?q=kittens`  


Note the `.../images/...` in B).


In A), I'm searching for images via the **web endpoint**.  
In B), I'm searching (without a type filter) via the dedicated **image endpoint**. 

The web endpoint is more versitile, but the image endpoint will provide richer information about images.

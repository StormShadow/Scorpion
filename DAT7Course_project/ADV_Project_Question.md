# Project Proposal: Predicting Conflicted Advice Based on SEC Form ADV Data

Using [methodology] (https://github.com/StormShadow/Scorpion/blob/master/DAT7Course_project/ADV%20Misleading%20Advertising%20Summary.pdf) from a previous project to identify misleading advertising as a starting point, I plan to examine the SEC's form ADV data to predict the likelihood of receiving the likelihood of receiving conflicted advise from a financial advisor based on data from SEC form ADV Part 1 and Part 2.

[Project Outline](https://github.com/StormShadow/Scorpion/blob/master/DAT7Course_project/Form%20ADV%20Project%20Outline.pdf)

*Project Question: Can you predict the likelihood of receiving conflicted advice by looking at form ADV data?*

*Brief background on SEC Form ADV and conflicted advice*

* The SEC collects information from registered investment advisor (RIA) firms including criteria such as products and services offered, assets under management, discplinary actions against them.  
* RIAs are generaly under a legal obligation to act under a fiducary standard of care, or in the best interest of a client.  
* However, there are instances where they can act under a lowe standard called the suitability standard.
* Due to disclusre requirements, language and information in the form ADV can reveal instances where there is a "conflict of interest" regarding the financial advice being given or product being sold.

*DATA Sources*

* Training Data Hand labled data** firms identified as engaging in misleading advertising of products and services, thus likely to give conflicted advice.  [DATA SOURCE CONFIDENTIAL will not be shared, essentially I will take the rows from ADV part 1, from source below and hand labeling them based on the findings]
* SEC Form ADV Part 1** publicly available data from SEC filtered and used to narrow sample size for training data availale [here](http://www.sec.gov/foia/docs/invafoia.htm)
* SEC Form ADV Part 2** individul forms available for download, however inquiring to availability of a bulk download of part 2 brochures for 11,000 plus RIA firms

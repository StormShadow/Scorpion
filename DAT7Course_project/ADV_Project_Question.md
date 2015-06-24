# Project Proposal: Predicting Conflicted Advice Based on SEC Form ADV Data

Using [methodology] (https://github.com/StormShadow/Scorpion/blob/master/DAT7Course_project/ADV%20Misleading%20Advertising%20Summary.pdf) from a previous project to identify misleading advertising as a starting point, I plan to examine the SEC's form ADV data to predict the likelihood of receiving conflicted advice from a financial advisor based on data from SEC form ADV Part 1 and Part 2.

[Project Outline Graphic](https://github.com/StormShadow/Scorpion/blob/master/DAT7Course_project/Form%20ADV%20Project%20Outline.pdf)

**Project Question: Can you predict the likelihood of receiving conflicted advice by looking at form ADV data?**

*Brief background on SEC Form ADV and conflicted advice*

* The SEC collects information from registered investment advisor (RIA) firms including criteria such as products and services offered, assets under management, disciplinary actions against them.  
* RIAs are generally under a legal obligation to act under a fiduciary standard of care, or in the best interest of a client.  
* However, there are instances where an RIA can act under a lower standard called the suitability standard but must disclose these events.
* There may also be instances where an RIA may say one thing, but carefully examining disclosures in the form ADV may reveal inconsistencies. 
* Due to disclosure requirements, language and information in the form ADV can reveal instances where there is a "conflict of interest" regarding the financial advice being given or financial product being sold.

*DATA Sources*

* Training Data - Hand labeled data of firms identified as engaging in misleading advertising of products and services, highly likely to give conflicted advice.  
**[DATA SOURCE CONFIDENTIAL will not be shared, essentially I will take the rows from ADV part 1, from source below and hand label them based on these findings]**
* SEC Form ADV Part 1 - Publicly available data from SEC filtered and initially used to narrow sample size for training data available [here](http://www.sec.gov/foia/docs/invafoia.htm).
* SEC Form ADV Part 2 - TBD if available.  Individual forms available for download, however inquiring to availability of a bulk download of part 2 brochures for 11,000 plus RIA firms.

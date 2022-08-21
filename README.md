# The-Great-Sentiment-Analyzer
Deployment Of Machine Learning Models Trained on Automatically Annotated Hindi and English Datasets

**Code authors: Aarav Babu, Aditi Singh, Atul Krishnan**

# Introduction:

The popularity of E-Commerce has grown multifold across the years since its inception. With the rise in traffic in such websites, there has been a growing dependency on the views and opinions of the products available. Companies and customers greatly rely on these reviews for sales, market demands, constructive criticism, and to check the quality of the product being bought. In our project, we’re looking at ways to avoid the manual labor involved in labeling the dataset through automatic annotating frameworks and are producing a dataset of Hindi reviews to help in the field of Sentiment Analysis in Indian Languages.

We have successfully trained a highly accurate model on data which was automatically annotated to segregate these reviews into Suggestions and Complaints. The custom ML model was then deployed to identify and classify the given reviews (both for a huge number and for single reviews). We are using FLASK API to run our deployment. It is free for research use and if you find it useful or use it in your research, please acknowledge our git repository.

# Table of Contents:

1. [Getting Started with deployment](#Getting-Started)
2. [About the Datasets, Automatic Annotation tools and Models](#About-the-Datasets,-Automatic-Annotation-Tools-and-Models)
3. [Future Scope](#Future-Scope)
4. [Contact us](#Contact-Us)

# Getting Started

1. To see the working model of our deployment, first download the zip file under /Deployment and extract it to the required folder.
2. Open command prompt in the folder path.
3. First pip install the “virtualenv” library in cmd using “pip install virtualenv”.
4. Create a new virtual environment using the command “virtualenv abc”.
    Alternate command “python -m virtualenv abc”.
3. To enter the virtual environment, use the “abc\Scripts\Activate” command where “abc” is the name of the virtual environment.
4. Once in virtualenv execute the command “pip install -r requirements.txt” to download all the dependencies.
5. Then run the following commands:
> set FLASK_APP=app.py (app name)
> 
> set FLASK_ENV=development
> 
> flask run
6. Copy and Paste the URL provided in the output screen onto any web browser.
7. Depending on the type of file you downloaded (Mass/Single), enter either a URL of        the product with its page number
 (for eg:      https://www.amazon.in/Vivo-Midnight-Additional-Exchange-Offers/product-reviews/B09Q5Z5M9D/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2) or a single review (for eg: “The phone is fast enough for daily use. Software needs much more improvement seems like some settings for UI is missing. Search inside settings won't show any results even if they exists”) .

**How to make your own .pkl file:**
1. Go to the /Deployment folder and then open the deployingmodel.ipynb file.
2. Change the Dataset to your own dataset.
3. Drop/Select whatever columns you want.
4. Use a classifier and estimator of your choice.
5. Run the full code.
6. Download the .pkl file from outputs and use it in your own deployment.

# About the Datasets, Automatic Annotation Tools and Models

The datasets have been provided under the /Datasets folder. All the reviews that we’ve used have been scraped by us using the python codes provided under the /Web Scraping folder. We have also created a one-of-a-kind Hindi/Hinglish balanced product reviews dataset that has also been web scraped (code provided) by us. It consists of 4331 reviews out of which 2284 were suggestions and 2047 were complaints.

We have provided the code for 3 Automatic Annotation Frameworks namely Vader, TextBlob, and Flair that we have used to label the datasets automatically under /AutomaticAnnotation folder. Our analysis across the 3 tools show that Flair was the better framework while TextBlob proved to be the fastest. Vader provided a good accuracy across datasets without much variance. 

The Automatically Annotated Datasets were then tried on various standard models to see the accuracy with which predictions can be made. On comparing the accuracies obtained, with a Manually labeled dataset, they were around a similar area which was very good. Bagging + XGBoosting gave the best accuracy which we used in the model we eventually deployed.

# Future Scope:

The field of opinion mining and sentiment analysis is among the most popular right now. In our study, we have shown the advantages of using Automatic Annotating Frameworks for labeling datasets to help ease the process, Published an exciting authentic Hindi/Hinglish review dataset that’ll help in further studies in SAIL. 
We have set the stage for a new set of studies in the field of Automatic Annotation in Indian Languages and helped build trust for it in English.
We hope you like our project and it helps you to work more in this field.

# Contact Us:

Atul Krishnan: atul.krishnan02@gmail.com

Aditi Singh: aditisingh02430@gmail.com

Aarav Babu: aaravbabu2002@gmail.com

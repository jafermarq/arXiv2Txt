# arXiv2Txt
Having access to thousands of publications via http://arxiv.org is great but when downloading a paper the title of the PDF document always comes in the form "1234.5675.pdf" or similar. That file name is the id fo the paper in the arXiv database. Here I present set of utils that automatically rename those PDFs with the title of the publication


### Getting ready 
   Here I make use of the python wrapper for the arXiv API provided by: https://github.com/lukasschwab/arxiv.py. You can install it as:
   
    $ pip install arxiv
    
   Among other options, this python wrapper allows to send a query to arXiv base on the id of the publication. We can use this query
   to obtain the title of the publication and then rename the original PDF.
   
   

### Renaming the .pdf

   This is the basic usage of the arxiv python package that we'll be using:
   
   ```python
    import arxiv
    
    paper_id = "1512.03385" # from a file "1512.03385.pdf"
    
    # send query to arXiv database and filter publication title
    paper_title = arxiv.query(id_list=[paper_id])[0]['title_detail']['value']
    
    print paper_title 
    # prints "Deep Residual Learning for Image Recognition"
   ```
   
### Usage

   Here I describe how to use each of the scripts int this repo. For each example, let's assume that the PDF file to rename is "1512.03385.pdf". The examples below assume that the PDF is in the same directory where the script is. However, this is not a requirement, passing a full path to the PDF will also work with either of the methods below.
   
 #### Python script
 
   ```python
     import getArXivName
     
     file_name = 1512.03385.pdf
     paper_title = getArXivName(file_name) 
     print paper_title # prints "Deep Residual Learning for Image Recognition"
     
     # your own code to rename the file
     ...
     
   ```

 #### Bash
 
    # This will rename the PDF file with the title of the publication, "Deep Residual Learning for Image Recognition" for this particular id
    $ ./rename.sh 1512.03385.pdf



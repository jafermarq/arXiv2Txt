# arXiv2Txt
Having access to thousands of publications via http://arxiv.org is great but when downloading a paper the title of the .pdf document always comes in the form "1234.5675.pdf" or similar. That file name is the id fo the paper in the arXiv database. Here I present set of utils that automatically rename those .pdf with the title of the publication


### Getting ready 
   Here I make use of the python wrapper for the arXiv API provided by: https://github.com/lukasschwab/arxiv.py. You can install it as:
   
    $ pip install arxiv
    
   Among other options, this python wrapper allows to send a query to arXiv base on the id of the publication. We can use this query
   to obtain the title of the publication and then rename the original pdf.
   
   
### Renaming the .pdf

   This is the basic usage of the arxiv python package that we'll be using:
   
   ```python
    import arxiv
    
    paper_id = "1512.03385" # from a file "1512.03385.pdf'
    
    # send query to arXiv database and filter publication title
    paper_title = arxiv.query(id_list=[paper_id])[0]['title_detail']['value']
    
    print paper_title 
    # prints "Deep Residual Learning for Image Recognition"
   ```

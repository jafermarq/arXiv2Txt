import sys
import arxiv
import ntpath


def main(file_name):
    fileName = ntpath.basename(sys.argv[1])
    arxiv_id = fileName[:fileName.rfind('.')]

    title = arxiv.query(id_list=[arxiv_id])[0]['title_detail']['value']
    print "arxiv_id:", arxiv_id
    print "Title:", title

    return title + ".pdf"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: $ python getArXicName.py <path-to-pdf-downloaded-from-arxiv>")
        print("\t*The pdf file is expected to have as name the arXiv id: e.g: '1709.02260.pdf'")
        exit()
    main(sys.argv[1])
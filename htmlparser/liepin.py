import bs4


def catchcv(htmlsource):
    bs = bs4.BeautifulSoup(htmlsource, 'lxml')
    side = bs.find(class_='side')
    side.decompose()
    footer = bs.find('footer')
    footer.decompose()
    javascripts = bs.findAll('script')
    for js in javascripts:
        js.decompose()
    alinks = bs.findAll('a')
    for a in alinks:
        a.decompose()
    content = bs.find(class_='resume')
    return content.prettify()
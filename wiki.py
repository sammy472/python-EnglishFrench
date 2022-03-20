import textwrap
import wikipedia 
def wikipedia_search(search,language='A'): 
    if language == 'A':
        wikipedia.set_lang('en')
    else:
        wikipedia.set_lang('fr')
    wrapper = textwrap.TextWrapper(width=60)
    try:
        m = wikipedia.summary(search,sentences=5)
        m = wrapper.fill(text=m)
        return m
    except:
        return "Search doesn't match anything."
if __name__ == '__main__':
    print(wikipedia_search('Bill Clinton','fr'))
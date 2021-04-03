import stanza


def get_stanza_model(processors=None, package='default', download=True):
    if download:
        stanza.download(lang='en', package=package, processors=processors)
    return stanza.Pipeline(lang='en', package=package, processors=processors)

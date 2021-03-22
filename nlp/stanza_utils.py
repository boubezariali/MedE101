import stanza


def get_stanza_model(processors, package='default', download=True):
    if download:
        stanza.download('en', package=package, processors=processors)
    return stanza.Pipeline('en', package=package, processors=processors)

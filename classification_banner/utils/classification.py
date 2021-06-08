def normalize(classification):
  classification = classification.lower().strip()
  return {
    'unclass':'unclass',
    'unclassified':'unclass',
    'secret':'secret',
    'sec':'secret',
    'ts':'ts',
    'top secret':'ts',
    'topsecret':'ts',
    'tssci':'tssci',
    'top secret sci':'tssci',
    'topsecretsci':'tssci',
    'tsscisap':'sapsar',
    'tsscisapsar':'sapsar',
    'sapsar':'sapsar',
    'sap':'sapsar',
    'sar':'sapsar',
    'tssap':'sapsar',
    'tssar':'sapsar',
  }[classification]

def get_style_class(classification):
  """Right now this is one to one"""
  return {
    'unclass': 'unclass',
    'secret': 'secret',
    'ts': 'ts',
    'tssci': 'tssci',
    'sapsar': 'sapsar',
  }[classification]

def format_classification_message(classification):
  return {
    'unclass': 'UNCLASSIFIED',
    'secret': 'SECRET',
    'ts': 'TOP SECRET',
    'tssci': 'TOP SECRET//SCI',
    'sapsar': 'TOP SECRET//SCI//SAP-SAR',
  }[classification]
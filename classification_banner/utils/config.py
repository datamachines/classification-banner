import yaml

def open_config(path="/etc/classification_banner/config.yaml"):
  with open(path, 'r') as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as exc:
      #TODO(mmay): real logging please
      print(exc)
      return None

def get_system_classification():
  config = open_config()
  try:
    return config['system']['classification']
  except:
    #TODO(mmay): real logging please
    print("system.classification not configured")
    return None

def get_classification_config(classification):
  config = open_config()
  try:
    return config['classifications'][classification]
  except:
    #TODO(mmay): real logging please
    print("Classifications information for %s not configured".format(classification))
    return None

def get_classification_label(classification):
  try:
    return get_classification_config(classification)['label']
  except:
    #TODO(mmay): real logging please
    print("Classification label for %s not configured".format(classification))
    return None

def get_classification_style_name(classification):
  try:
    return get_classification_config(classification)['style']
  except:
    #TODO(mmay): real logging please
    print("Classification style for %s not configured".format(classification))
    return None
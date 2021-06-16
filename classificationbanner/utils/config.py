import logging
logger = logging.getLogger("classificationbanner")

import yaml

def open_config(path="/etc/classification-banner/config.yaml"):
  with open(path, 'r') as stream:
    try:
      return yaml.safe_load(stream)
    except yaml.YAMLError as err:
      logger.error(err)
      return None

def get_system_classification(config):
  try:
    return config['system']['classification']
  except:
    logger.error("System's classification not configured")
    return None

def get_classification_config(config, classification):
  try:
    return config['classifications'][classification]
  except:
    logger.error("Classifications information for \"{}\" not configured".format(classification))
    return None

def get_classification_label(config, classification):
  try:
    return get_classification_config(config, classification)['label']
  except:
    logger.error("Classification label for \"{}\" not configured".format(classification))
    return None

def get_classification_style_name(config, classification):
  try:
    return get_classification_config(config, classification)['style']
  except:
    logger.error("Classification style for \"{}\" not configured".format(classification))
    return None

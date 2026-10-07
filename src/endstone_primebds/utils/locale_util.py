import json
import os
from endstone_primebds.utils.config_util import CONFIG_FOLDER, open_text_file

_locales = {}
_current_lang = "en_US"
_initialized = False

def init_locales():
    global _current_lang, _locales, _initialized
    if _initialized:
        return
    _initialized = True
    
    # Load language config
    from endstone_primebds.utils.config_util import load_config, save_config
    config = load_config()
    lang = config.get("language", "en_US")
    if "language" not in config:
        config["language"] = "en_US"
        save_config(config)
    
    _current_lang = lang
    
    # Base directory for locales inside plugin src
    current_dir = os.path.dirname(os.path.abspath(__file__))
    locales_dir = os.path.join(os.path.dirname(current_dir), "locales")
    
    if os.path.exists(locales_dir):
        for file in os.listdir(locales_dir):
            if file.endswith(".json"):
                lang_code = file[:-5]
                try:
                    content = open_text_file(os.path.join(locales_dir, file), "r")
                    if content:
                        _locales[lang_code] = json.loads(content)
                except Exception as e:
                    print(f"[Onistone Essentials] Failed to load locale {file}: {e}")

def tr(key, default_en, **kwargs):
    """
    Get localized string by key. Falls back to en_US, then to default_en.
    Uses kwargs for string formatting.
    """
    init_locales()
    text = default_en
    if _current_lang in _locales and key in _locales[_current_lang]:
        text = _locales[_current_lang][key]
    elif "en_US" in _locales and key in _locales["en_US"]:
        text = _locales["en_US"][key]
        
    if kwargs:
        try:
            return text.format(**kwargs)
        except KeyError:
            pass # fallback to unformatted if keys mismatch
    return text

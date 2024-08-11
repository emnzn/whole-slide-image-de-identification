# De-identification Script for Whole Slide Images

**NOTE:** Can only work for *.svs* whole slide image formats at the moment.

## Installation
```bash
pip install -r requirements.txt
```

## Configuration

Configure source and destination folders by providing their paths in `config.yaml`.

``` yaml
source_dir: path/to/your/svs/files
dest_dir: path/to/save/your/de-identified/images
```

## De-identification
```bash
python convert.py
```

## To-Do:
- [ ] Add support for other source image formats.
# De-identification Script for Whole Slide Images

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
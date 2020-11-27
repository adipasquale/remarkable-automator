# ReMarkable upload script & Mac OS Automator Workflows

This tiny Python3 script uses [rmapy](https://github.com/subutux/rmapy) to upload files to the ReMarkable cloud. You can then use this script with Mac OS Automator workflows:

1. a tiny app to select and upload files
2. (more interestingly) a "Folder Action" that will upload all EPUB files downloaded

This works nicely with the [epub-press](https://github.com/haroldtreen/epub-press-clients) browser extensions that lets you create EPUB books easily from your browser

## Install

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Initial Config

Head to [https://my.remarkable.com/connect/desktop](my.remarkable.com/connect/desktop), copy the 6 letter code and call the register_device.py script:

```sh
source venv/bin/activate
python3 register_device.py xxxxxx
```

This will create a `~/.rmapi` with a token that wilsl authenticate you in the future.

## CLI Usage

To upload a file (PDF or EPUB):

```sh
source venv/bin/activate
python3 upload_file.py /path/to/file.epub
```

## Automator Workflows (Apple Mac OS only)

### 1. Regular Workflow

You can try copying the `./remarkable-upload-file.workflow` file and see if it works out-of-the box for you, you may have to rewrite paths.

![remarkable-upload-file.workflow](https://raw.githubusercontent.com/adipasquale/remarkable-automator/main/remarkable-upload-file.workflow/Contents/QuickLook/Preview.png)

### 2. Folder Action : auto-upload all downloaded EPUB

Again, you can try copying the `./remarkable-upload-file.workflow` file and see if it works out-of-the box for you, you may have to rewrite paths.

![upload-downloaded-ebook-to-remarkable.workflow](https://raw.githubusercontent.com/adipasquale/remarkable-automator/main/upload-downloaded-ebook-to-remarkable.workflow/Contents/QuickLook/Preview.png)

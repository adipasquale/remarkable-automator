# ReMarkable upload script & Mac OS Automator Workflows

This tiny script uses [rmapy](https://github.com/subutux/rmapy) to upload files to the Remarkable cloud. You can then use this script with Mac OS Automator workflows:

- to have a tiny app that you can call, select a file and have it uploaded without opening the Remarkable Desktop app
- or more interestingly by using a "Folder Action" that will upload all EPUB files downloaded to your ReMarkable reader.

This last script works really nicely with the [epub-press](https://github.com/haroldtreen/epub-press-clients) browser extensions that let you create EPUB books easily from your browser

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

![](./remarkable-upload-file.workflow/QuickLook/Preview.png)

### 2. Folder Action : auto-upload all downloaded EPUB

Again, you can try copying the `./remarkable-upload-file.workflow` file and see if it works out-of-the box for you, you may have to rewrite paths.

![](./upload-downloaded-ebook-to-remarkable.workflow/QuickLook/Preview.png)

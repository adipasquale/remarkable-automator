# ReMarkable upload script & Mac OS Automator Workflows

This tiny Python3 script uses [rmapy](https://github.com/subutux/rmapy) to upload files to the ReMarkable cloud. You can then use this script with Mac OS Automator workflows:

1. App: select Finder items & upload
2. Quick Action: right-click shortcut in Finder
3. Folder Action : auto-upload downloaded EPUB files

This works nicely together with the [epub-press](https://github.com/haroldtreen/epub-press-clients) browser extensions that lets you create EPUB books easily from your browser

## Install

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Initial Config

Head to [my.remarkable.com/connect/desktop](https://my.remarkable.com/connect/desktop), copy the 6 letter code and call the register_device.py script:

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

### 1. App: select Finder items & upload

Simply open `./remarkable-upload.app`. It should ask you to select file(s) and upload them.

### 2. Quick Action: right-click shortcut in Finder

Install quick action by opening `./remarkable-upload-quick-action.workflow`. A prompt should appear and ask you to confirm. You should now see a new quick action appear when you right click items in the finder:

![screenshot quick action](https://raw.githubusercontent.com/adipasquale/remarkable-automator/main/screenshot-quick-action.png)


### 3. Folder Action : auto-upload downloaded EPUB files

Install quick action by opening `./remarkable-auto-upload.workflow`. A prompt should appear and ask you to confirm.

All EPUB files created in the `~/Downloads` folder should now be automatically uploaded.

![remarkable-auto-upload.workflow](https://raw.githubusercontent.com/adipasquale/remarkable-automator/main/remarkable-auto-upload.workflow/Contents/QuickLook/Preview.png)

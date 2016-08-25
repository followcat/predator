# Predator

Lightweight crawler framework based on template analysis.

## Dependencies

    APScheduler==3.1.0
    beautifulsoup4==4.4.1
    dulwich==0.12.0
    PyYAML==3.11
    selenium==2.53.2

Need to install cyaml to support CSafeDumper/CSafeLoader.

## Downloader

    Support urllib downloader and webdriver downloader.
    Set cookies to login when using urllib.
    Set profile path to login when using webdriver download.

## Parser

    Use beautifulsoup to parse downloaded html.

## Storage

    Use filesystem or git interface to storage data.

## Develop

    Downloader/Parser/Storage can be very simple to customize.
    Add-on functions 'development by using Class inheritance.

## DEMO

    The project has a number of examples of climbing up cv,
    you can call them by using these command:

    Download CV:

        python tools/plan.py jobs.cv.youprojectname sources.industry_needed

    Download Classify:

        python tools/plan.py jobs.classify.youprojectname sources.industry_needed

    You can add several files you need ,but this files should be split by ',' , such as:

        python tools/plan.py jobs.classify.youprojectname sources.industry1,sources.industry2,sources.industry3

    You can resume download by add '-r' or '--resume' like this:

        python tools/plan.py jobs.classify.youprojectname sources.industry_needed -r

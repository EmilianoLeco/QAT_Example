import os
import shutil
from time import strftime
from features.pages.home_page import *
from features.pages.search_results import *


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results = SearchResultsPage()


def after_all(context):
    print("User data:", context.config.userdata)
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                strftime("%d_%m_%Y"),'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")
    context.browser.close()

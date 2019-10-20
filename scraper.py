from get_colors import get_page_colors
from get_urls import open_scroll_collect_posts, get_page_urls_from_posts
from save_data import create_save_json

NUM_SITES_TO_GET = 9

if __name__ == "__main__":

    # open the browser to collect post links from producthunt 
    posts = open_scroll_collect_posts(int(NUM_SITES_TO_GET / 9))

    # get the urls to the projects from the producthunt post pages
    print("Getting website links")
    urls = get_page_urls_from_posts(posts)

    colors = []

    # get the colors from each of the project pages 
    print("Getting colors from websites")
    for url in urls:
        try:
            colors.append(get_page_colors(url))
        except e:
            print("An error ocurred getting a page's colors")
            continue

    # create the json file
    print("Saving data")
    create_save_json(colors)

    print("Done, got colors from {} websites".format(len(colors)))

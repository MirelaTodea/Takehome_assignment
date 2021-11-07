# This file is used to run check_popular_searches_links.py
from check_popular_searches_links.check_popular_searches_links import CheckPopularSearches


def swt_tc_001_check_popular_searches_links():
    '''
    -TESTDESCRIPTION-
    <INTENT>                The intent of this test case is to check that the Popular Searches
                            links are working correctly.
                            </INTENT>

    <PRECONDITION>          - </PRECONDITION>

    <ACTION>                [1] Open bayut.com.
                            [2] Scroll down to the Popular searches section on the homepage.
                            [3] Open the To rent tab.
                            [4] Validate visible links under Dubai apartments are functioning correctly.
                            [5.1] Press View all button to make all the links under Dubai
                            apartments visible.
                            [5.2] Validate hidden links under Dubai apartments are functioning correctly.

                            </ACTION>

    <EXPECTED_RESULT>       [1] The web page is loaded.
                            [2] The web page is scrolled until Popular searches field is into view.
                            [3] Popular searches to rent are displayed.
                            [4] Print all visible links that are working properly.
                            [5.1] All links are visible.
                            [5.2] Print all hidden links are working properly.
                            </EXPECTED_RESULT>

    <POSTCONDITION>         - </POSTCONDITION>

    <AUTHOR_DESCRIPTION>    Todea Mirela </AUTHOR_DESCRIPTION>

    <AUTHOR_CODE>           Todea Mirela </AUTHOR_CODE>

    <TESTMETHODS>           REQUIREMENT_BASED </TESTMETHODS>

    <STATUS_TD>             READY_FOR_REVIEW </STATUS_TD>

    <STATUS_TC>             READY_FOR_REVIEW </STATUS_TC>

    <BUG_TICKETS>           - </BUG_TICKETS>
    '''

    bot = CheckPopularSearches()
    bot.land_first_page()
    bot.scroll_down_to_popular_searches()
    bot.select_popular_searches_to_rent()
    bot.validate_visible_links()
    bot.view_all_links()
    bot.validate_hidden_links()


if __name__ == "__main__":
    swt_tc_001_check_popular_searches_links()

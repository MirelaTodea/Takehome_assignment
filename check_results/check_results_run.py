# This file is used to run check_results.py from test case
from check_results.check_results import CheckResults


def swt_tc_001_check_results():
    '''
    -TESTDESCRIPTION-
    <INTENT>                The intent of this test case is to check that the results match
                            the search criteria.
                            </INTENT>

    <PRECONDITION>          - </PRECONDITION>

    <ACTION>                [1] Open bayut.com.
                            [2] Select Dubai Marina as a location.
                            [3] Select properties For Sale.
                            [4] Search for properties.
                            [5] Verify that all displayed properties contain the selected location.
                            </ACTION>

    <EXPECTED_RESULT>       [1] The web page is loaded.
                            [2] Dubai Marina is selected in the location field.
                            [3] Properties type is selected.
                            [4] The page with the results is loaded.
                            [5] All the properties are printed.
                            </EXPECTED_RESULT>

    <POSTCONDITION>         - </POSTCONDITION>

    <AUTHOR_DESCRIPTION>    Todea Mirela </AUTHOR_DESCRIPTION>

    <AUTHOR_CODE>           Todea Mirela </AUTHOR_CODE>

    <TESTMETHODS>           REQUIREMENT_BASED </TESTMETHODS>

    <STATUS_TD>             READY_FOR_REVIEW </STATUS_TD>

    <STATUS_TC>             READY_FOR_REVIEW </STATUS_TC>

    <BUG_TICKETS>           - </BUG_TICKETS>
    '''

    bot = CheckResults()
    bot.land_first_page()
    bot.select_location("Dubai", " Marina")
    bot.properties_for_sale()
    bot.find_properties_with_all_attributes()
    bot.verify_location("Dubai Marina")

if __name__ == "__main__":
    swt_tc_001_check_results()
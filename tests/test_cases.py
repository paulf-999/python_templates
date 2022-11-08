import TODO_snowflake_client as snowflake_client


####################################################################
# PyTests
####################################################################
# use the below to provide test_cases
def test_sf_conn_bad_credentials():
    """ trivial example """
    # TODO - need tests to validate the exceptions thrown
    assert snowflake_client.create_snowflake_connection()

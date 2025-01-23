class ConfigQuery:
    SELECT_MY_CONFIG = """
    SELECT
        p1.email
        ,p2.first_name
        ,p2.first_name_ruby
        ,p2.last_name
        ,p2.last_name_ruby
        ,p2.zip_code
        ,p2.state
        ,p2.city
        ,p2.address
        ,p2.phone_number
        ,p2.birthday
    FROM
        usr.user p1
        INNER JOIN usr.user_info p2 on p1.id = p2.id and not p2.delete_flag
    WHERE
        p1.username = %s
        and not p1.delete_flag        
    """

    UPDATE_MY_CONFIG_FOR_USER = """
    UPDATE usr.user p1
    SET email = %(email)s
    WHERE
        p1.username = %(username)s
        and not p1.delete_flag
    """


    UPDATE_MY_CONFIG_FOR_USER_INFO = """
    UPDATE usr.user_info p1
    SET
        first_name = %(first_name)s
        ,first_name_ruby = %(first_name_ruby)s
        ,last_name = %(last_name)s
        ,last_name_ruby = %(last_name_ruby)s
        ,full_name = %(full_name)s
        ,full_name_ruby = %(first_name_ruby)s 
        ,zip_code = %(zip_code)s
        ,state = %(state)s
        ,city = %(city)s
        ,address = %(address)s
        ,phone_number = %(phone_number)s
        ,birthday = %(birthday)s
    FROM usr.user p2
    WHERE
        p1.id = p2.id
        and p2.username = %(username)s
        and not p1.delete_flag
        and not p2.delete_flag
    """

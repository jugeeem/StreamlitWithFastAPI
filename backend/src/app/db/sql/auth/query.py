class AuthQuery:
    """
    認証関連のSQLを定義するクラス
    """

    EXISTS_USER = """
    SELECT
        p1.username as username
    FROM usr.user p1
    WHERE
        exists(
            SELECT r1.*
            FROM usr.user r1
            WHERE
                p1.id = r1.id
                and r1.username = %s
                and not r1.delete_flag
        )
    """

    INSERT_USR_USER = """
    INSERT INTO usr.user(
        email
        ,username
        ,password

        ,role_id
    )
    VALUES (
        %s
        ,%s
        ,%s

        ,%s
    )
    """

    INSERT_USR_USER_INFO = """
    INSERT INTO usr.user_info(id)
    SELECT p1.id
    FROM usr.user p1
    WHERE
        p1.username = %s
        and not p1.delete_flag
    """

    SELECT_SIGNIN = """
    SELECT
        p1.name
        ,p1.role_id
    FROM usr.user p1
    WHERE
        p1.name = %s
        and p1.password = %s
        and not p1.delete_flag
    """

    GET_USER = """
    SELECT
        p1.username as username
        ,p1.email as email
        ,p2.full_name as full_name
        ,p1.disabled as disabled
        ,p1.password as hashed_password
    FROM
        usr.user p1
        INNER JOIN usr.user_info p2 on p1.id = p2.id
    WHERE
        p1.username = %s
        and not p1.delete_flag
    """

    GET_USER_ID = """
    SELECT
        p1.id as id
    FROM usr.user p1
    WHERE
        p1.name = %s
        and not p1.delete_flag
    order by p1.id asc
    limit 1
    """
